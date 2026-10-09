# Proje 8: Soğuk Zincir Sıcaklık Kaydı — Raspberry Pi Pico W (MicroPython)
from machine import Pin
import onewire, ds18x20
import network, socket, json, time

SSID = "AG_ADI"
SIFRE = "SIFRENIZ"

ow = onewire.OneWire(Pin(15))
ds = ds18x20.DS18X20(ow)
ROM = ds.scan()[0]        # bağlı ilk sensör
ESIK = 8.0               # °C — üstüne çıkarsa uyarı

def wifi_baglan():
    """Pico W'yi ağa bağlar ve IP adresini yazdırır."""
    w = network.WLAN(network.STA_IF)
    w.active(True)
    w.connect(SSID, SIFRE)
    while not w.isconnected():
        time.sleep(0.5)
    print("IP adresi:", w.ifconfig()[0])

def olcum():
    """Sensörden veri okur, sözlük döndürür."""
    ds.convert_temp()
    time.sleep_ms(750)
    t = ds.read_temp(ROM)
    with open("log.csv", "a") as f:
        f.write("{},{}\n".format(time.time(), round(t, 1)))
    return {"sicaklik": round(t, 1), "esik_asimi": t > ESIK}

def cevap(c, govde):
    c.send("HTTP/1.0 200 OK\r\nContent-Type: application/json\r\n\r\n" + json.dumps(govde))

def sunucu():
    """Port 8080'de HTTP sunucusu."""
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", 8080))
    s.listen(2)
    print("Sunucu hazır: http://<pico-ip>:8080/data")
    while True:
        c, _ = s.accept()
        try:
            istek = c.recv(1024).decode()
            yol = istek.split(" ")[1] if " " in istek else "/"
            if yol.startswith("/data"):
                cevap(c, olcum())
            elif yol.startswith("/log"):
                try:
                    satirlar = open("log.csv").readlines()[-10:]
                except OSError:
                    satirlar = []
                cevap(c, {"satirlar": satirlar})
            else:
                cevap(c, {"hata": "bilinmeyen yol"})
        except Exception as e:
            print("istek hatası:", e)
        finally:
            c.close()

wifi_baglan()
sunucu()

# Proje 16: Sıcaklığa Göre Fan Otomasyonu — Raspberry Pi Pico W (MicroPython)
from machine import Pin
import onewire, ds18x20
import network, socket, json, time

SSID = "AG_ADI"
SIFRE = "SIFRENIZ"

ow = onewire.OneWire(Pin(15))
ds = ds18x20.DS18X20(ow)
ROM = ds.scan()[0]
fan = Pin(17, Pin.OUT)
ESIK = 30.0           # °C
MOD = {"otomatik": True, "manuel": 0}

def wifi_baglan():
    """Pico W'yi ağa bağlar, IP adresini yazdırır."""
    w = network.WLAN(network.STA_IF)
    w.active(True)
    w.connect(SSID, SIFRE)
    while not w.isconnected():
        time.sleep(0.5)
    print("IP adresi:", w.ifconfig()[0])

def olcum():
    """Durum bilgisini sözlük olarak döndürür."""
    ds.convert_temp()
    time.sleep_ms(750)
    t = round(ds.read_temp(ROM), 1)
    if MOD["otomatik"]:
        fan.value(1 if t > ESIK else 0)
    else:
        fan.value(MOD["manuel"])
    return {"sicaklik": t, "esik": ESIK, "fan": fan.value(), "otomatik": MOD["otomatik"]}

def cevap(c, govde):
    c.send("HTTP/1.0 200 OK\r\nContent-Type: application/json\r\n\r\n" + json.dumps(govde))

def sunucu():
    """HTTP sunucusu: /data (oku) ve komut yolları."""
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
            elif yol.startswith("/mod"):
                MOD["otomatik"] = "o=1" in yol
                cevap(c, MOD)
            elif yol.startswith("/fan"):
                MOD["otomatik"] = False
                MOD["manuel"] = 1 if "d=1" in yol else 0
                fan.value(MOD["manuel"])
                cevap(c, MOD)
            else:
                cevap(c, {"hata": "bilinmeyen yol"})
        except Exception as e:
            print("istek hatası:", e)
        finally:
            c.close()

wifi_baglan()
sunucu()

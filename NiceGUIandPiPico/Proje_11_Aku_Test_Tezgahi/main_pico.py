# Proje 11: Akü Test Tezgahı — Raspberry Pi Pico W (MicroPython)
from machine import Pin, ADC
import network, socket, json, time

SSID = "AG_ADI"
SIFRE = "SIFRENIZ"

yuk = Pin(16, Pin.OUT)        # röle ile deşarj yükü
v_adc = ADC(Pin(26))         # gerilim bölücü
i_adc = ADC(Pin(27))         # ACS712 akım sensörü
TEST = {"aktif": False, "baslangic": 0}

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
    volt = round(v_adc.read_u16() * 3.3 / 65535 * 5, 2)
    akim = round((i_adc.read_u16() * 3.3 / 65535 - 1.65) / 0.066, 2)
    sure = time.time() - TEST["baslangic"] if TEST["aktif"] else 0
    return {"volt": volt, "akim": akim, "sure": round(sure, 1),
            "enerji_wh": round(volt * akim * sure / 3600, 3), "test": TEST["aktif"]}

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
            elif yol.startswith("/test"):
                TEST["aktif"] = "b=1" in yol
                TEST["baslangic"] = time.time()
                yuk.value(1 if TEST["aktif"] else 0)
                cevap(c, {"test": TEST["aktif"]})
            else:
                cevap(c, {"hata": "bilinmeyen yol"})
        except Exception as e:
            print("istek hatası:", e)
        finally:
            c.close()

wifi_baglan()
sunucu()

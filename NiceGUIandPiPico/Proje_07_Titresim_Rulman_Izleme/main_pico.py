# Proje 7: Titreşim ile Rulman Arıza İzleme — Raspberry Pi Pico W (MicroPython)
from machine import I2C, Pin
import mpu6050   # kütüphaneyi Pico'ya kopyalayın
import math
import network, socket, json, time

SSID = "AG_ADI"
SIFRE = "SIFRENIZ"

i2c = I2C(0, sda=Pin(4), scl=Pin(5))
sensor = mpu6050.MPU6050(i2c)
ESIK = 0.35    # g cinsinden sapma eşiği

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
    ornekler = []
    for _ in range(20):
        a = sensor.get_accel_data()
        ornekler.append(math.sqrt(a["x"]**2 + a["y"]**2 + a["z"]**2))
        time.sleep_ms(10)
    ort = sum(ornekler) / len(ornekler)
    sapma = (sum((x - ort) ** 2 for x in ornekler) / len(ornekler)) ** 0.5
    return {"ivme": round(ort, 3), "sapma": round(sapma, 3), "alarm": sapma > ESIK}

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
            else:
                cevap(c, {"hata": "bilinmeyen yol"})
        except Exception as e:
            print("istek hatası:", e)
        finally:
            c.close()

wifi_baglan()
sunucu()

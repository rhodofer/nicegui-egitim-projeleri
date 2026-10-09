# Proje 13: Kapı / Bariyer Kontrolü (RFID) — Raspberry Pi Pico W (MicroPython)
from machine import Pin, SPI, PWM
from mfrc522 import MFRC522   # kütüphaneyi Pico'ya kopyalayın
import time
import network, socket, json, time

SSID = "AG_ADI"
SIFRE = "SIFRENIZ"

spi = SPI(0, baudrate=100000, sck=Pin(2), mosi=Pin(3), miso=Pin(4))
rdr = MFRC522(spi, Pin(5))
servo = PWM(Pin(17))
servo.freq(50)
YETKILI = ["a1b2c3d4"]     # izinli kart UID listesi
SON = {"kart": "", "durum": "kapali"}

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
    uid, _ = rdr.read_id_noauth()
    kart = "{:08x}".format(uid) if uid else ""
    if kart:
        SON["kart"] = kart
        SON["durum"] = "acik" if kart in YETKILI else "reddedildi"
        servo.duty_u16(4915 if SON["durum"] == "acik" else 3277)   # 90° / 0°
        time.sleep(3)
        servo.duty_u16(3277)
    return {"son_kart": SON["kart"], "durum": SON["durum"]}

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
            elif yol.startswith("/kapi"):
                servo.duty_u16(4915)
                SON["durum"] = "acik"
                time.sleep(3)
                servo.duty_u16(3277)
                SON["durum"] = "kapali"
                cevap(c, {"durum": "kapali"})
            else:
                cevap(c, {"hata": "bilinmeyen yol"})
        except Exception as e:
            print("istek hatası:", e)
        finally:
            c.close()

wifi_baglan()
sunucu()

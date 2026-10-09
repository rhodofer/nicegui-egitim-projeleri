# Proje 17: RFID Yoklama Okuyucu — Raspberry Pi Pico W (MicroPython)
from machine import Pin, SPI
from mfrc522 import MFRC522
import network, socket, json, time

SSID = "AG_ADI"
SIFRE = "SIFRENIZ"

spi = SPI(0, baudrate=100000, sck=Pin(2), mosi=Pin(3), miso=Pin(4))
rdr = MFRC522(spi, Pin(5))
SON = {"uid": ""}

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
    if uid:
        SON["uid"] = "{:08x}".format(uid)
    return {"uid": SON["uid"]}

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
            else:
                cevap(c, {"hata": "bilinmeyen yol"})
        except Exception as e:
            print("istek hatası:", e)
        finally:
            c.close()

wifi_baglan()
sunucu()

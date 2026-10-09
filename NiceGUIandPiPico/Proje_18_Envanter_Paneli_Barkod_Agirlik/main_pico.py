# Proje 18: Envanter Terminali (Barkod + Ağırlık) — Raspberry Pi Pico W (MicroPython)
from machine import Pin, UART
from hx711 import HX711   # kütüphaneyi Pico'ya kopyalayın
import network, socket, json, time

SSID = "AG_ADI"
SIFRE = "SIFRENIZ"

okuyucu = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))   # barkod okuyucu
hx = HX711(dout=Pin(20), pd_sck=Pin(21))
SON = {"barkod": "", "agirlik": 0.0}

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
    if okuyucu.any():
        SON["barkod"] = okuyucu.readline().decode().strip()
    SON["agirlik"] = round(hx.get_weight(5) / 1000, 2)   # gram → kg
    return SON

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

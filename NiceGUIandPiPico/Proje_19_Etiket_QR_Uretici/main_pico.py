# Proje 19: Termal Yazıcı Sürücü (Etiket Basma) — Raspberry Pi Pico W (MicroPython)
from machine import Pin, UART
import network, socket, json, time

SSID = "AG_ADI"
SIFRE = "SIFRENIZ"

yazici = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
DURUM = {"son": ""}

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
    return {"durum": "hazır", "son_etiket": DURUM["son"]}

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
            elif yol.startswith("/yaz"):
                metin = yol.split("metin=")[1].replace("%20", " ").replace("%0A", "\n")
                yazici.write(b"\x1b@" + metin.encode() + b"\n\n\n" + b"\x1dV\x00")
                DURUM["son"] = metin
                cevap(c, {"durum": "basildi", "metin": metin})
            else:
                cevap(c, {"hata": "bilinmeyen yol"})
        except Exception as e:
            print("istek hatası:", e)
        finally:
            c.close()

wifi_baglan()
sunucu()

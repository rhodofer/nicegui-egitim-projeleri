# Proje 15: Sulama Zamanlayıcı — Raspberry Pi Pico W (MicroPython)
from machine import Pin, RTC
import network, socket, json, time

SSID = "AG_ADI"
SIFRE = "SIFRENIZ"

pompa = Pin(16, Pin.OUT)
rtc = RTC()
PROGRAM = []          # [["07:30", 120], ...] saat + saniye
AKTIF = {"sulama": False, "kalan": 0}

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
    saat = "{:02d}:{:02d}".format(rtc.datetime()[4], rtc.datetime()[5])
    return {"saat": saat, "program": PROGRAM, "sulama": AKTIF["sulama"]}

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
            elif yol.startswith("/ekle"):
                saat = yol.split("saat=")[1].split("&")[0].replace("%3A", ":")
                sure = int(yol.split("sure=")[1])
                PROGRAM.append([saat, sure])
                cevap(c, {"program": PROGRAM})
            elif yol.startswith("/simdi"):
                AKTIF["sulama"] = True
                pompa.value(1)
                time.sleep(5)
                pompa.value(0)
                AKTIF["sulama"] = False
                cevap(c, {"sulama": False})
            else:
                cevap(c, {"hata": "bilinmeyen yol"})
        except Exception as e:
            print("istek hatası:", e)
        finally:
            c.close()

wifi_baglan()
sunucu()

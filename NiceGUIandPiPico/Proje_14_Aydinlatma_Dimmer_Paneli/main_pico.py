# Proje 14: Aydınlatma Dimmer Paneli — Raspberry Pi Pico W (MicroPython)
from machine import Pin, PWM
import network, socket, json, time

SSID = "AG_ADI"
SIFRE = "SIFRENIZ"

led = PWM(Pin(16))
led.freq(20000)          # göz kırpmayı önlemek için yüksek frekans
DURUM = {"duty": 0}

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
    return {"duty": DURUM["duty"]}

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
            elif yol.startswith("/duty"):
                d = int(yol.split("d=")[1]) if "d=" in yol else 0
                d = max(0, min(100, d))
                DURUM["duty"] = d
                led.duty_u16(int(d / 100 * 65535))
                cevap(c, DURUM)
            else:
                cevap(c, {"hata": "bilinmeyen yol"})
        except Exception as e:
            print("istek hatası:", e)
        finally:
            c.close()

wifi_baglan()
sunucu()

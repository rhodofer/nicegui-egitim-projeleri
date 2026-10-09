# Proje 12: Motor Kontrol Paneli — Raspberry Pi Pico W (MicroPython)
from machine import Pin, PWM
import network, socket, json, time

SSID = "AG_ADI"
SIFRE = "SIFRENIZ"

motor = PWM(Pin(16))
motor.freq(1000)
yon1 = Pin(17, Pin.OUT)
yon2 = Pin(18, Pin.OUT)
DURUM = {"duty": 0, "yon": "dur"}

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
    return {"duty": DURUM["duty"], "yon": DURUM["yon"]}

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
            elif yol.startswith("/pwm"):
                d = int(yol.split("d=")[1].split("&")[0]) if "d=" in yol else 0
                d = max(0, min(100, d))
                DURUM["duty"] = d
                motor.duty_u16(int(d / 100 * 65535))
                if "yon=ileri" in yol:
                    yon1.value(1); yon2.value(0); DURUM["yon"] = "ileri"
                elif "yon=geri" in yol:
                    yon1.value(0); yon2.value(1); DURUM["yon"] = "geri"
                elif d == 0:
                    yon1.value(0); yon2.value(0); DURUM["yon"] = "dur"
                cevap(c, DURUM)
            else:
                cevap(c, {"hata": "bilinmeyen yol"})
        except Exception as e:
            print("istek hatası:", e)
        finally:
            c.close()

wifi_baglan()
sunucu()

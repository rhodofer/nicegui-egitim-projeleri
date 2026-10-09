# Proje 5: Su Deposu Seviyesi (HC-SR04) — Raspberry Pi Pico W (MicroPython)
from machine import Pin
import machine
import network, socket, json, time

SSID = "AG_ADI"          # kendi Wi-Fi ağınız
SIFRE = "SIFRENIZ"

trig = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
DEPO_YUKSEKLIK = 100   # cm

def wifi_baglan():
    """Pico W'yi ağa bağlar, IP adresini yazdırır."""
    w = network.WLAN(network.STA_IF)
    w.active(True)
    w.connect(SSID, SIFRE)
    while not w.isconnected():
        time.sleep(0.5)
    print("IP adresi:", w.ifconfig()[0])   # NiceGUI bu adrese bağlanacak

def olcum():
    """Sensörden veri okur ve sözlük döndürür."""
    trig.value(0); time.sleep_us(2); trig.value(1); time.sleep_us(10); trig.value(0)
    sure = machine.time_pulse_us(echo, 1, 30000)   # mikrosaniye
    mesafe = round(sure * 0.0343 / 2, 1)           # ses hızı
    yuzde = round(max(0, min(100, (DEPO_YUKSEKLIK - mesafe) * 100 / DEPO_YUKSEKLIK)), 1)
    return {"mesafe_cm": mesafe, "doluluk": yuzde}

def cevap(c, govde, tip="application/json"):
    """Tarayıcıya HTTP yanıtı yazar."""
    c.send("HTTP/1.0 200 OK\r\nContent-Type: " + tip + "\r\n\r\n" + json.dumps(govde))

def sunucu():
    """Port 8080'de basit HTTP sunucusu: /data ve /set yollarını dinler."""
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", 8080))
    s.listen(2)
    print("Sunucu hazır: http://<pico-ip>:8080/data")
    while True:
        c, _ = s.accept()                 # bağlantı bekle
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
            c.close()                     # bağlantıyı kapat

wifi_baglan()      # önce ağa bağlan
sunucu()           # sonra sunucuyu başlat (sonsuz döngü)

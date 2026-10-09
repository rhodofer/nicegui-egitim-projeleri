# Proje 3: Sera İklim Kontrolü — Raspberry Pi Pico W (MicroPython)
import dht
from machine import Pin, ADC
import network, socket, json, time

SSID = "AG_ADI"          # kendi Wi-Fi ağınız
SIFRE = "SIFRENIZ"

sensor = dht.DHT22(Pin(15))
fan = Pin(17, Pin.OUT)
light_adc = ADC(Pin(27))

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
    sensor.measure()
    return {"sicaklik": sensor.temperature(), "nem": sensor.humidity(),
            "isik": round(light_adc.read_u16() * 100 / 65535, 1),
            "fan": fan.value()}

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
            elif yol.startswith("/fan"):
                durum = 1 if "d=1" in yol else 0
                fan.value(durum)
                cevap(c, {"fan": durum})
            else:
                cevap(c, {"hata": "bilinmeyen yol"})
        except Exception as e:
            print("istek hatası:", e)
        finally:
            c.close()                     # bağlantıyı kapat

wifi_baglan()      # önce ağa bağlan
sunucu()           # sonra sunucuyu başlat (sonsuz döngü)

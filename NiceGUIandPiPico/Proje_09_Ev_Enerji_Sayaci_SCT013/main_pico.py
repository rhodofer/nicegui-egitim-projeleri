# Proje 9: Ev Enerji Sayacı (SCT-013) — Raspberry Pi Pico W (MicroPython)
from machine import Pin, ADC
import math
import network, socket, json, time

SSID = "AG_ADI"
SIFRE = "SIFRENIZ"

akim_adc = ADC(Pin(26))    # SCT-013 + yük direnci ile gerilime çevrilir
SEBEKE = 230.0
ORNEK = 200
defset = 0.5               # ADC orta noktası kalibrasyonu

def wifi_baglan():
    """Pico W'yi ağa bağlar ve IP adresini yazdırır."""
    w = network.WLAN(network.STA_IF)
    w.active(True)
    w.connect(SSID, SIFRE)
    while not w.isconnected():
        time.sleep(0.5)
    print("IP adresi:", w.ifconfig()[0])

kWh = 0.0

def olcum():
    """Sensörden veri okur, sözlük döndürür."""
    global kWh
    ham = [akim_adc.read_u16() for _ in range(ORNEK)]
    ort = sum(ham) / len(ham)
    rms = (sum((x - ort) ** 2 for x in ham) / len(ham)) ** 0.5
    akim = round(rms * 30 / 65535, 3)      # 30 A ölçekli sensör
    guc = round(akim * SEBEKE, 1)
    kWh += guc / 1000 / 3600 * (ORNEK * 0.0002)   # örnekleme süresi kadar enerji
    return {"akim": akim, "guc": guc, "kWh": round(kWh, 4)}

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

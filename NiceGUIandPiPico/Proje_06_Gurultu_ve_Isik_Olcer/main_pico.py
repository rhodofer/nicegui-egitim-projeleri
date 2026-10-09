# Proje 6: Gürültü ve Işık Ölçer — Raspberry Pi Pico W (MicroPython)
from machine import Pin, ADC
import network, socket, json, time

SSID = "AG_ADI"
SIFRE = "SIFRENIZ"

ses_adc = ADC(Pin(26))     # mikrofon/amplifikatör çıkışı
isik_adc = ADC(Pin(27))    # LDR gerilim bölücü

def wifi_baglan():
    """Pico W'yi ağa bağlar ve IP adresini yazdırır."""
    w = network.WLAN(network.STA_IF)
    w.active(True)
    w.connect(SSID, SIFRE)
    while not w.isconnected():
        time.sleep(0.5)
    print("IP adresi:", w.ifconfig()[0])

def olcum():
    """Sensörden veri okur, sözlük döndürür."""
    ses = round(ses_adc.read_u16() * 100 / 65535, 1)      # 0-100 bağıl seviye
    isik = round(isik_adc.read_u16() * 100 / 65535, 1)
    return {"ses": ses, "isik": isik}

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

# Proje 10: Solar Şarj İzleyici — Raspberry Pi Pico W (MicroPython)
from machine import Pin, ADC
import network, socket, json, time

SSID = "AG_ADI"
SIFRE = "SIFRENIZ"

v_adc = ADC(Pin(26))       # panel gerilimi (bölücü ile ~1/6)
i_adc = ADC(Pin(27))       # şönt üzerinden akım
AKU_KAPASITE_AH = 7.2      # örnek: 12 V 7.2 Ah

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
    volt = round(v_adc.read_u16() * 3.3 / 65535 * 6, 2)      # 6x bölücü
    akim = round((i_adc.read_u16() * 3.3 / 65535 - 1.65) / 0.1, 2)
    guc = round(volt * akim, 2)
    soc = round(max(0, min(100, (volt - 11.8) * 100 / (12.8 - 11.8))), 1)
    return {"volt": volt, "akim": akim, "guc": guc, "soc": soc, "kapasite_ah": AKU_KAPASITE_AH}

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

# Proje 1: Sıcaklık-Nem Paneli — NiceGUI arayüzü
import random, requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"   # Pico'nun IP adresini buraya yazın
SIM = True                          # donanım yoksa True: simülasyon verisi üretir
gecmis_t, gecmis_n = [], []         # grafik için geçmiş değerler

def veri_oku():
    """Pico'dan /data adresini okur; hata olursa None döner."""
    if SIM:
        return {"sicaklik": round(random.uniform(21, 26), 1),
                "nem": round(random.uniform(40, 60), 1)}
    try:
        return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception:
        return None

@ui.page("/")
def ana():
    ui.label("Sıcaklık / Nem Paneli").classes("text-h5")
    with ui.row():
        sicaklik_et = ui.label("--").classes("text-h3 text-primary")
        nem_et = ui.label("--").classes("text-h3 text-secondary")
    grafik = ui.echart({"xAxis": {"type": "category", "data": []},
                        "yAxis": {"type": "value"},
                        "series": [{"type": "line", "data": [], "name": "Sıcaklık (°C)"}]}
                       ).style("height:260px;width:100%")
    durum = ui.label("bekleniyor...").classes("text-caption")

    def guncelle():
        v = veri_oku()
        if v is None:
            durum.set_text("Pico'ya bağlanılamadı (IP/simülasyon ayarını kontrol edin)")
            return
        sicaklik_et.set_text(f"{v['sicaklik']} °C")
        nem_et.set_text(f"{v['nem']} %")
        durum.set_text("bağlı · son güncelleme az önce")
        gecmis_t.append(v["sicaklik"])
        if len(gecmis_t) > 30: gecmis_t.pop(0)
        grafik.options["series"][0]["data"] = gecmis_t
        grafik.options["xAxis"]["data"] = [str(i) for i in range(len(gecmis_t))]
        grafik.update()

    ui.timer(2.0, guncelle, immediate=True)     # 2 saniyede bir veri çek


import os
if os.environ.get("SELFTEST"):
    for _ in range(3):
        print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="Sıcaklık-Nem Paneli", port=8080, show=False, reload=False)

# Proje 8: Soğuk Zincir Kaydı — NiceGUI arayüzü
import random, requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"
SIM = True
ESIK = 8.0
kayitlar = []

def veri_oku():
    if SIM:
        return {"sicaklik": round(random.uniform(2, 12), 1), "esik_asimi": None}
    try:
        return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception:
        return None

@ui.page("/")
def ana():
    ui.label("Soğuk Zincir Sıcaklık Kaydı").classes("text-h5")
    with ui.row():
        sic_et = ui.label("-- °C").classes("text-h3")
        durum = ui.label("").classes("text-subtitle1")
    tablo = ui.table(columns=[{"name": "saat", "label": "Ölçüm", "field": "saat"},
                              {"name": "sicaklik", "label": "Sıcaklık (°C)", "field": "sicaklik", ":sortable": True},
                              {"name": "durum", "label": "Durum", "field": "durum"}],
                     rows=[], row_key="saat").classes("w-full")

    def guncelle():
        v = veri_oku()
        if v is None: return
        t = v["sicaklik"]
        sic_et.set_text(f"{t} °C")
        asimi = t > ESIK
        durum.set_text("⚠️ Eşik aşıldı" if asimi else "Normal aralıkta").classes("text-negative" if asimi else "text-positive")
        kayitlar.append({"saat": f"#{len(kayitlar) + 1}", "sicaklik": t,
                         "durum": "EŞİK AŞIMI" if asimi else "normal"})
        tablo.rows = kayitlar[-15:]
        tablo.update()

    ui.timer(2.0, guncelle, immediate=True)

import os
if os.environ.get("SELFTEST"):
    for _ in range(3): print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="Soğuk Zincir", port=8080, show=False, reload=False)

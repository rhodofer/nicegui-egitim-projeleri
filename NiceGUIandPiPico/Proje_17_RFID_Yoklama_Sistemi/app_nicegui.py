# Proje 17: RFID Yoklama Sistemi — NiceGUI arayüzü
import random, requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"
SIM = True
OGRENCILER = {"a1b2c3d4": "Ayşe Yılmaz", "b2c3d4e5": "Mehmet Demir", "c3d4e5f6": "Zeynep Kaya"}
yoklama = {}

def veri_oku():
    if SIM:
        return {"uid": random.choice(list(OGRENCILER) + ["00000000"])}
    try:
        return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception:
        return None

@ui.page("/")
def ana():
    ui.label("RFID Yoklama").classes("text-h5")
    with ui.row().classes("items-center"):
        son_et = ui.label("son okuma: -").classes("text-h6")
        sayac = ui.label("yoklama: 0").classes("text-caption")
    tablo = ui.table(columns=[{"name": "no", "label": "No", "field": "no"},
                              {"name": "ad", "label": "Ad Soyad", "field": "ad"},
                              {"name": "durum", "label": "Durum", "field": "durum"}],
                     rows=[{"no": i + 1, "ad": ad, "durum": "—"} for i, ad in enumerate(OGRENCILER.values())],
                     row_key="no").classes("w-full")

    def guncelle():
        v = veri_oku()
        if v is None: return
        uid = v["uid"]
        ad = OGRENCILER.get(uid, "tanınmayan kart")
        son_et.set_text(f"son okuma: {ad}")
        if uid in OGRENCILER:
            yoklama[uid] = True
        satirlar = [{"no": i + 1, "ad": a, "durum": "GELDİ" if k in yoklama else "—"}
                    for i, (k, a) in enumerate(OGRENCILER.items())]
        tablo.rows = satirlar
        tablo.update()
        sayac.set_text(f"yoklama: {len(yoklama)}/{len(OGRENCILER)}")

    ui.timer(2.0, guncelle, immediate=True)

import os
if os.environ.get("SELFTEST"):
    for _ in range(3): print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="RFID Yoklama", port=8080, show=False, reload=False)

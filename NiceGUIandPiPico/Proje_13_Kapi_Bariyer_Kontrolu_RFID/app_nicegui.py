# Proje 13: Kapı Kontrolü — NiceGUI arayüzü
import random, requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"
SIM = True
gecisler = []

def veri_oku():
    if SIM:
        if random.random() < 0.3:
            kart = "a1b2c3d4" if random.random() < 0.7 else "ff00ff00"
            gecisler.append({"kart": kart, "durum": "izinli" if kart == "a1b2c3d4" else "reddedildi"})
        return {"son_kart": (gecisler[-1]["kart"] if gecisler else "-"),
                "durum": (gecisler[-1]["durum"] if gecisler else "bekliyor")}
    try:
        return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception:
        return None

@ui.page("/")
def ana():
    ui.label("Kapı / Bariyer Kontrolü").classes("text-h5")
    with ui.row().classes("items-center"):
        kart_et = ui.label("son kart: -").classes("text-h6")
        durum_et = ui.label("").classes("text-subtitle1")
        ui.button("Kapıyı aç", icon="lock_open",
                  on_click=lambda: (requests.get(f"{PICO}/kapi?ac=1", timeout=1.0)
                                    if not SIM else None))
    tablo = ui.table(columns=[{"name": "kart", "label": "Kart UID", "field": "kart"},
                              {"name": "durum", "label": "Sonuç", "field": "durum"}],
                     rows=[], row_key="kart").classes("w-full")

    def guncelle():
        v = veri_oku()
        if v is None: return
        kart_et.set_text(f"son kart: {v['son_kart']}")
        durum_et.set_text(v["durum"])
        durum_et.classes(replace="text-negative" if v["durum"] == "reddedildi" else "text-positive")
        tablo.rows = gecisler[-15:]
        tablo.update()

    ui.timer(2.0, guncelle, immediate=True)

import os
if os.environ.get("SELFTEST"):
    for _ in range(3): print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="Kapı Kontrolü", port=8080, show=False, reload=False)

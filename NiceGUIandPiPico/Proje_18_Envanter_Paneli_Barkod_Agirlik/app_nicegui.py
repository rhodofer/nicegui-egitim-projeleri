# Proje 18: Envanter Panelı (Barkod + Ağırlık) — NiceGUI arayüzü
import random, requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"
SIM = True
envanter = [{"barkod": "8680001", "ad": "Direnç 1k", "adet": 120, "min": 50},
            {"barkod": "8680002", "ad": "Kondansatör 100nF", "adet": 30, "min": 40},
            {"barkod": "8680003", "ad": "LM317", "adet": 12, "min": 10}]

def veri_oku():
    if SIM:
        return {"barkod": random.choice(["8680001", "8680002", "9999999"]),
                "agirlik": round(random.uniform(0.05, 1.2), 2)}
    try:
        return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception:
        return None

@ui.page("/")
def ana():
    ui.label("Laboratuvar Envanteri").classes("text-h5")
    with ui.row():
        barkod_et = ui.label("barkod: -").classes("text-h6")
        agirlik_et = ui.label("ağırlık: - kg").classes("text-caption")
    arama = ui.input("Ara (malzeme adı)").props("clearable")
    tablo = ui.table(columns=[{"name": "barkod", "label": "Barkod", "field": "barkod"},
                              {"name": "ad", "label": "Malzeme", "field": "ad"},
                              {"name": "adet", "label": "Adet", "field": "adet", ":sortable": True},
                              {"name": "durum", "label": "Durum", "field": "durum"}],
                     rows=[], row_key="barkod").classes("w-full")

    def listele():
        q = (arama.value or "").lower()
        satirlar = [dict(m, durum=("DÜŞÜK STOK" if m["adet"] < m["min"] else "yeterli"))
                    for m in envanter if q in m["ad"].lower()]
        tablo.rows = satirlar
        tablo.update()

    arama.on_value_change(lambda e: listele())
    listele()

    def guncelle():
        v = veri_oku()
        if v is None: return
        barkod_et.set_text(f"barkod: {v['barkod']}")
        agirlik_et.set_text(f"ağırlık: {v['agirlik']} kg")
        for m in envanter:
            if m["barkod"] == v["barkod"]:
                m["adet"] += 1
        listele()

    ui.timer(3.0, guncelle, immediate=True)

import os
if os.environ.get("SELFTEST"):
    for _ in range(3): print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="Envanter Paneli", port=8080, show=False, reload=False)

# Proje 6: Gürültü ve Işık Ölçer — NiceGUI arayüzü
import random, requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"
SIM = True
ESIK = 70

def veri_oku():
    if SIM:
        return {"ses": round(random.uniform(20, 95), 1), "isik": round(random.uniform(5, 100), 1)}
    try:
        return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception:
        return None

@ui.page("/")
def ana():
    ui.label("Ortam Ölçümü (Ses / Işık)").classes("text-h5")
    with ui.card().classes("w-full"):
        ses_et = ui.label("ses: --").classes("text-h6")
        ses_bar = ui.linear_progress(value=0)
        isik_et = ui.label("ışık: --").classes("text-h6")
        isik_bar = ui.linear_progress(value=0).props("color=amber")
    gunluk = ui.log(max_lines=8).style("height:160px")

    def guncelle():
        v = veri_oku()
        if v is None: return
        ses_bar.value = v["ses"] / 100
        isik_bar.value = v["isik"] / 100
        ses_et.set_text(f"ses: {v['ses']} (bağıl)")
        isik_et.set_text(f"ışık: {v['isik']} (bağıl)")
        if v["ses"] > ESIK:
            gunluk.push(f"⚠️ Yüksek ses: {v['ses']}")

    ui.timer(2.0, guncelle, immediate=True)

import os
if os.environ.get("SELFTEST"):
    for _ in range(3): print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="Ortam Ölçümü", port=8080, show=False, reload=False)

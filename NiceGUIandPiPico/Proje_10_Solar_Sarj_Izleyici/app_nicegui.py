# Proje 10: Solar Şarj İzleyici — NiceGUI arayüzü
import random, requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"
SIM = True

def veri_oku():
    if SIM:
        volt = round(random.uniform(11.9, 14.2), 2)
        akim = round(random.uniform(0.1, 3.5), 2)
        return {"volt": volt, "akim": akim, "guc": round(volt * akim, 2),
                "soc": round(max(0, min(100, (volt - 11.8) * 100)), 1), "kapasite_ah": 7.2}
    try:
        return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception:
        return None

@ui.page("/")
def ana():
    ui.label("Solar Şarj İzleyici").classes("text-h5")
    with ui.row():
        with ui.card():
            ui.label("Panel gerilimi").classes("text-caption")
            v_et = ui.label("-- V").classes("text-h4")
        with ui.card():
            ui.label("Şarj akımı").classes("text-caption")
            a_et = ui.label("-- A").classes("text-h4")
        with ui.card():
            ui.label("Güç").classes("text-caption")
            w_et = ui.label("-- W").classes("text-h4")
    with ui.row().classes("items-center"):
        soc_bar = ui.circular_progress(value=0, min=0, max=100, show_value=True, size="150px")
        with ui.column():
            soc_et = ui.label("-- %").classes("text-h4")
            not_et = ui.label("").classes("text-caption")

    def guncelle():
        v = veri_oku()
        if v is None: return
        v_et.set_text(f"{v['volt']} V")
        a_et.set_text(f"{v['akim']} A")
        w_et.set_text(f"{v['guc']} W")
        soc_bar.value = v["soc"]
        soc_et.set_text(f"{v['soc']} %")
        not_et.set_text(f"Batarya: 12 V / {v['kapasite_ah']} Ah")

    ui.timer(2.0, guncelle, immediate=True)

import os
if os.environ.get("SELFTEST"):
    for _ in range(3): print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="Solar Şarj İzleyici", port=8080, show=False, reload=False)

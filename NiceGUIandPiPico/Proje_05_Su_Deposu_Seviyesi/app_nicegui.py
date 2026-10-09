# Proje 5: Su Deposu Seviyesi — NiceGUI arayüzü
import random, requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"
SIM = True
ALARM = 20      # % altına düşerse uyarı

def veri_oku():
    if SIM:
        return {"mesafe_cm": round(random.uniform(10, 90), 1),
                "doluluk": round(random.uniform(5, 100), 1)}
    try:
        return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception:
        return None

@ui.page("/")
def ana():
    ui.label("Su Deposu Seviyesi").classes("text-h5")
    with ui.row().classes("items-center"):
        gosterge = ui.circular_progress(value=0, min=0, max=100, show_value=True,
                                        size="180px").props("color=primary")
        with ui.column():
            seviye = ui.label("-- %").classes("text-h3")
            mesafe = ui.label("-- cm").classes("text-caption")
            uyari = ui.label("").classes("text-subtitle1")

    def guncelle():
        v = veri_oku()
        if v is None: return
        gosterge.value = v["doluluk"] / 100
        seviye.set_text(f"{v['doluluk']} %")
        mesafe.set_text(f"yüzeye uzaklık: {v['mesafe_cm']} cm")
        if v["doluluk"] < ALARM:
            uyari.set_text("⚠️ Seviye kritik — depo beslenmeli").classes("text-negative")
        else:
            uyari.set_text("Seviye normal").classes("text-positive")

    ui.timer(2.0, guncelle, immediate=True)


import os
if os.environ.get("SELFTEST"):
    for _ in range(3):
        print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="Su Seviyesi", port=8080, show=False, reload=False)

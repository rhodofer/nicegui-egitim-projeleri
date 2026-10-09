# Proje 16: Fan Otomasyonu — NiceGUI arayüzü
import random, requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"
SIM = True
durum = {"otomatik": True, "manuel": 0}

def komut(yol: str):
    if not SIM:
        try: requests.get(f"{PICO}{yol}", timeout=1.0)
        except Exception: pass

def veri_oku():
    if SIM:
        t = round(random.uniform(24, 34), 1)
        fan = 1 if (t > 30 and durum["otomatik"]) else durum["manuel"]
        return {"sicaklik": t, "esik": 30.0, "fan": fan, "otomatik": durum["otomatik"]}
    try:
        return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception:
        return None

@ui.page("/")
def ana():
    ui.label("Fan Otomasyonu").classes("text-h5")
    sic_et = ui.label("-- °C").classes("text-h3")
    fan_et = ui.label("").classes("text-subtitle1")
    mod = ui.radio(["Otomatik", "Manuel"], value="Otomatik").props("inline")
    manuel = ui.switch("Fanı aç (manuel)", on_change=lambda e: komut(f"/fan?d={1 if e.value else 0}"))
    esik_goster = ui.label("otomatik eşik: 30 °C").classes("text-caption")

    def guncelle():
        v = veri_oku()
        if v is None: return
        sic_et.set_text(f"{v['sicaklik']} °C")
        fan_et.set_text("fan: AÇIK" if v["fan"] else "fan: kapalı")
        fan_et.classes(replace="text-negative" if v["fan"] else "text-positive")

    ui.timer(2.0, guncelle, immediate=True)
    mod.on_value_change(lambda e: (durum.update(otomatik=e.value == "Otomatik"),
                                   komut(f"/mod?o={1 if e.value == 'Otomatik' else 0}")))

import os
if os.environ.get("SELFTEST"):
    for _ in range(3): print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="Fan Otomasyonu", port=8080, show=False, reload=False)

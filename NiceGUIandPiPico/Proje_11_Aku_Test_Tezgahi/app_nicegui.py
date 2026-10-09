# Proje 11: Akü Test Tezgahı — NiceGUI arayüzü
import random, requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"
SIM = True
egri = {"sure": [], "volt": []}

def veri_oku():
    if SIM:
        return {"volt": round(random.uniform(11.5, 12.8), 2), "akim": round(random.uniform(0.8, 2.5), 2),
                "sure": len(egri["sure"]) * 2, "enerji_wh": round(len(egri["sure"]) * 0.01, 3), "test": True}
    try:
        return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception:
        return None

def test_kontrol(baslat: bool):
    if not SIM:
        try: requests.get(f"{PICO}/test?b={1 if baslat else 0}", timeout=1.0)
        except Exception: pass

@ui.page("/")
def ana():
    ui.label("Akü Test Tezgahı").classes("text-h5")
    with ui.row():
        ui.button("Testi başlat", icon="play_arrow", on_click=lambda: test_kontrol(True))
        ui.button("Durdur", icon="stop", color="negative", on_click=lambda: test_kontrol(False))
    with ui.grid(columns=3):
        with ui.card():
            ui.label("Gerilim").classes("text-caption"); v_et = ui.label("-- V").classes("text-h4")
        with ui.card():
            ui.label("Akım").classes("text-caption"); a_et = ui.label("-- A").classes("text-h4")
        with ui.card():
            ui.label("Enerji").classes("text-caption"); e_et = ui.label("-- Wh").classes("text-h4")
    grafik = ui.echart({"xAxis": {"type": "category", "data": []}, "yAxis": {"type": "value"},
                        "series": [{"type": "line", "data": [], "name": "Gerilim (V)"}]}).style("height:250px;width:100%")
    durum = ui.label("test bekleniyor").classes("text-caption")

    def guncelle():
        v = veri_oku()
        if v is None: return
        v_et.set_text(f"{v['volt']} V"); a_et.set_text(f"{v['akim']} A"); e_et.set_text(f"{v['enerji_wh']} Wh")
        durum.set_text(f"test {'aktif' if v['test'] else 'durdu'} · {v['sure']} s")
        egri["sure"].append(v["sure"]); egri["volt"].append(v["volt"])
        egri["sure"] = egri["sure"][-40:]; egri["volt"] = egri["volt"][-40:]
        grafik.options["series"][0]["data"] = egri["volt"]
        grafik.options["xAxis"]["data"] = [str(s) for s in egri["sure"]]
        grafik.update()

    ui.timer(2.0, guncelle, immediate=True)

import os
if os.environ.get("SELFTEST"):
    for _ in range(3): print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="Akü Testi", port=8080, show=False, reload=False)

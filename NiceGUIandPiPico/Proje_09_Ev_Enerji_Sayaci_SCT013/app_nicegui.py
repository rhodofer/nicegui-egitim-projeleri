# Proje 9: Enerji Sayacı — NiceGUI arayüzü
import random, requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"
SIM = True
gecmis_guc = []

def veri_oku():
    if SIM:
        guc = round(random.uniform(80, 900), 1)
        gecmis_guc.append(guc)
        if len(gecmis_guc) > 30: gecmis_guc.pop(0)
        return {"akim": round(guc / 230, 3), "guc": guc, "kWh": round(sum(gecmis_guc) / 1000 / 1800, 4)}
    try:
        return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception:
        return None

@ui.page("/")
def ana():
    ui.label("Ev Enerji Sayacı").classes("text-h5")
    with ui.grid(columns=3):
        with ui.card():
            ui.label("Anlık güç").classes("text-caption")
            guc_et = ui.label("-- W").classes("text-h4 text-primary")
        with ui.card():
            ui.label("Akım").classes("text-caption")
            akim_et = ui.label("-- A").classes("text-h4")
        with ui.card():
            ui.label("Toplam enerji").classes("text-caption")
            kwh_et = ui.label("-- kWh").classes("text-h4 text-secondary")
    grafik = ui.echart({"xAxis": {"type": "category", "data": []}, "yAxis": {"type": "value"},
                        "series": [{"type": "bar", "data": [], "name": "Güç (W)"}]}).style("height:260px;width:100%")

    def guncelle():
        v = veri_oku()
        if v is None: return
        guc_et.set_text(f"{v['guc']} W")
        akim_et.set_text(f"{v['akim']} A")
        kwh_et.set_text(f"{v['kWh']} kWh")
        if SIM:
            grafik.options["series"][0]["data"] = gecmis_guc
            grafik.options["xAxis"]["data"] = [str(i) for i in range(len(gecmis_guc))]
            grafik.update()

    ui.timer(2.0, guncelle, immediate=True)

import os
if os.environ.get("SELFTEST"):
    for _ in range(3): print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="Enerji Sayacı", port=8080, show=False, reload=False)

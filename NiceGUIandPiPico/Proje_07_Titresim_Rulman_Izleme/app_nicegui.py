# Proje 7: Titreşim İzleme — NiceGUI arayüzü
import random, requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"
SIM = True
gecmis = []

def veri_oku():
    if SIM:
        sapma = round(abs(random.gauss(0.25, 0.12)), 3)
        return {"ivme": 1.0, "sapma": sapma, "alarm": sapma > 0.35}
    try:
        return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception:
        return None

@ui.page("/")
def ana():
    ui.label("Titreşim / Rulman İzleme").classes("text-h5")
    with ui.row().classes("items-center"):
        gosterge = ui.knob(value=0, min=0, max=1, step=0.01, size="160px", show_value=True)
        with ui.column():
            sapma_et = ui.label("--").classes("text-h4")
            durum = ui.label("").classes("text-subtitle1")
    grafik = ui.echart({"xAxis": {"type": "category", "data": []}, "yAxis": {"type": "value"},
                        "series": [{"type": "line", "data": [], "name": "Titreşim sapması (g)"}]}).style("height:240px;width:100%")

    def guncelle():
        v = veri_oku()
        if v is None: return
        gosterge.value = v["sapma"]
        sapma_et.set_text(f"sapma: {v['sapma']} g")
        if v["alarm"]:
            durum.set_text("⚠️ ALARM: titreşim eşiğin üzerinde").classes("text-negative")
        else:
            durum.set_text("normal").classes("text-positive")
        gecmis.append(v["sapma"])
        if len(gecmis) > 40: gecmis.pop(0)
        grafik.options["series"][0]["data"] = gecmis
        grafik.options["xAxis"]["data"] = [str(i) for i in range(len(gecmis))]
        grafik.update()

    ui.timer(2.0, guncelle, immediate=True)

import os
if os.environ.get("SELFTEST"):
    for _ in range(3): print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="Titreşim İzleme", port=8080, show=False, reload=False)

# Proje 4: Hava İstasyonu (BME280) — NiceGUI arayüzü
import random, requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"
SIM = True
kayit = {"basinc": [], "nem": []}

def veri_oku():
    """Pico'daki /data ucundan sıcaklık, basınç ve nem okur."""
    if SIM:
        kayit["basinc"] = (kayit["basinc"] + [round(random.uniform(1005, 1015), 1)])[-30:]
        kayit["nem"] = (kayit["nem"] + [round(random.uniform(40, 60), 1)])[-30:]
        return {"sicaklik": round(random.uniform(18, 24), 1),
                "basinc": kayit["basinc"][-1], "nem": kayit["nem"][-1]}
    try:
        return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception:
        return None

@ui.page("/")
def ana():
    ui.label("Hava İstasyonu").classes("text-h5")
    with ui.row():
        with ui.card():
            ui.label("Sıcaklık").classes("text-caption")
            sic = ui.label("--").classes("text-h4 text-primary")
        with ui.card():
            ui.label("Basınç").classes("text-caption")
            bas = ui.label("--").classes("text-h4 text-secondary")
        with ui.card():
            ui.label("Nem").classes("text-caption")
            nem = ui.label("--").classes("text-h4 text-accent")
    grafik = ui.echart({"xAxis": {"type": "category", "data": []}, "yAxis": {"type": "value"},
                        "series": [{"type": "line", "name": "Basınç (hPa)", "data": []},
                                   {"type": "line", "name": "Nem (%)", "data": []}]}
                       ).style("height:280px;width:100%")

    def guncelle():
        v = veri_oku()
        if v is None:
            return
        sic.set_text(f"{v['sicaklik']} °C")
        bas.set_text(f"{v['basinc']} hPa")
        nem.set_text(f"{v['nem']} %")
        grafik.options["series"][0]["data"] = kayit["basinc"] if SIM else grafik.options["series"][0]["data"] + [v["basinc"]]
        grafik.options["series"][1]["data"] = kayit["nem"] if SIM else grafik.options["series"][1]["data"] + [v["nem"]]
        grafik.options["xAxis"]["data"] = [str(i + 1) for i in range(len(grafik.options["series"][0]["data"]))]
        grafik.update()

    ui.timer(2.0, guncelle, immediate=True)

import os
if os.environ.get("SELFTEST"):
    for _ in range(3):
        print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="Hava İstasyonu", port=8080, show=False, reload=False)

# Proje 3: Sera İklim Kontrolü — NiceGUI arayüzü
import random, requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"
SIM = True
ayar = {"sicaklik_ust": 28.0, "nem_alt": 40.0}

def veri_oku():
    if SIM:
        return {"sicaklik": round(random.uniform(20, 30), 1),
                "nem": round(random.uniform(35, 65), 1),
                "isik": round(random.uniform(10, 90), 1), "fan": 0}
    try:
        return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception:
        return None

def fan_yaz(durum: int):
    if not SIM:
        try: requests.get(f"{PICO}/fan?d={durum}", timeout=1.0)
        except Exception: pass

@ui.page("/")
def ana():
    ui.label("Sera İklim Paneli").classes("text-h5")
    with ui.grid(columns=3):
        sic = ui.label("--").classes("text-h4")
        nem = ui.label("--").classes("text-h4")
        isik = ui.label("--").classes("text-h4")
    with ui.card():
        ui.label("Eşik ayarları").classes("text-subtitle2")
        ui.number("Sıcaklık üst eşiği (°C)", value=ayar["sicaklik_ust"], step=0.5,
                  on_change=lambda e: ayar.update(sicaklik_ust=e.value))
        ui.number("Nem alt eşiği (%)", value=ayar["nem_alt"], step=1,
                  on_change=lambda e: ayar.update(nem_alt=e.value))
    gunluk = ui.log(max_lines=8).style("height:150px")
    fan_sw = ui.switch("Fan", on_change=lambda e: fan_yaz(1 if e.value else 0))

    def guncelle():
        v = veri_oku()
        if v is None:
            gunluk.push("Pico'ya bağlanılamadı"); return
        sic.set_text(f"{v['sicaklik']} °C")
        nem.set_text(f"{v['nem']} %")
        isik.set_text(f"{v['isik']} lx")
        if v["sicaklik"] > ayar["sicaklik_ust"] and not fan_sw.value:
            fan_sw.value = True                    # eşik aşıldı: fanı aç
            gunluk.push(f"Fan açıldı (sıcaklık {v['sicaklik']} °C)")

    ui.timer(2.0, guncelle, immediate=True)


import os
if os.environ.get("SELFTEST"):
    for _ in range(3):
        print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="Sera Paneli", port=8080, show=False, reload=False)

# Proje 15: Sulama Zamanlayıcı — NiceGUI arayüzü
import requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"
SIM = True
program = [{"saat": "07:30", "sure": 120}, {"saat": "19:00", "sure": 90}]

def veri_oku():
    """Cihaz saatini ve programı okur."""
    if SIM:
        return {"saat": "09:12", "program": program, "sulama": False}
    try:
        return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception:
        return None

def program_ekle(saat, sure):
    """Programı listeye ekler ve Pico'ya bildirir."""
    program.append({"saat": str(saat), "sure": int(sure)})
    if not SIM:
        try: requests.get(f"{PICO}/ekle?saat={saat}&sure={sure}", timeout=1.0)
        except Exception: pass

@ui.page("/")
def ana():
    ui.label("Sulama Zamanlayıcı").classes("text-h5")
    with ui.row().classes("items-center"):
        saat_et = ui.label("--").classes("text-h4")
        ui.button("Şimdi sula", icon="water_drop",
                  on_click=lambda: (ui.notify("Sulama başladı (5 sn)"),
                                    None if SIM else requests.get(f"{PICO}/simdi", timeout=6.0)))
    with ui.card():
        ui.label("Yeni program").classes("text-subtitle2")
        giris = ui.time(value="07:00")
        sure = ui.number("Süre (saniye)", value=60, min=5, max=600, step=5)
        tablo = ui.table(columns=[{"name": "saat", "label": "Saat", "field": "saat"},
                                  {"name": "sure", "label": "Süre (sn)", "field": "sure"}],
                         rows=list(program), row_key="saat").classes("w-full")

        def ekle():
            program_ekle(giris.value, sure.value)
            tablo.rows = list(program)     # satırlar sözlük listesi olmalı
            tablo.update()

        ui.button("Ekle", icon="add", on_click=ekle)

    def guncelle():
        v = veri_oku()
        if v:
            saat_et.set_text(f"cihaz saati: {v['saat']}")

    ui.timer(3.0, guncelle, immediate=True)

import os
if os.environ.get("SELFTEST"):
    for _ in range(3): print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="Sulama Zamanlayıcı", port=8080, show=False, reload=False)

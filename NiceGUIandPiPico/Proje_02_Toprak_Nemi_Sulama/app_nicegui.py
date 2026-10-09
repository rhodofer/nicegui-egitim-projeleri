# Proje 2: Toprak Nemi ve Otomatik Sulama — NiceGUI arayüzü
import random, requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"
SIM = True
ESIK = {"deger": 35}        # nem bu değerin altına düşerse sulama önerilir

def veri_oku():
    if SIM:
        return {"nem": round(random.uniform(25, 70), 1), "pompa": 0}
    try:
        return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception:
        return None

def pompaya_yaz(deger: int):
    """Pico'ya pompa komutu gönderir (SIM açıkken yalnızca arayüzde tutulur)."""
    if not SIM:
        try: requests.get(f"{PICO}/pompa?d={deger}", timeout=1.0)
        except Exception: pass

@ui.page("/")
def ana():
    ui.label("Sulama Paneli").classes("text-h5")
    nem = ui.linear_progress(value=0, show_value=False).props("instant-feedback")
    nem_et = ui.label("-- %").classes("text-h4")
    durum = ui.label("").classes("text-caption")
    pompa_sw = ui.switch("Pompa (manuel)", on_change=lambda e: pompaya_yaz(1 if e.value else 0))
    esik_in = ui.number("Nem eşiği (%)", value=ESIK["deger"], min=0, max=100, step=1)

    def guncelle():
        v = veri_oku()
        if v is None:
            durum.set_text("Pico'ya bağlanılamadı"); return
        nem.value = v["nem"] / 100
        nem_et.set_text(f"{v['nem']} %")
        if v["nem"] < esik_in.value:
            durum.set_text("⚠️ Nem eşiğin altında — sulama gerekli").classes("text-negative")
        else:
            durum.set_text("Nem yeterli").classes("text-positive")

    ui.timer(2.0, guncelle, immediate=True)


import os
if os.environ.get("SELFTEST"):
    for _ in range(3):
        print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="Sulama Paneli", port=8080, show=False, reload=False)

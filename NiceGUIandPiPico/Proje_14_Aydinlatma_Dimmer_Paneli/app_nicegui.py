# Proje 14: Aydınlatma Dimmer Paneli — NiceGUI arayüzü
import requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"
SIM = True
durum = {"duty": 0}

def parlaklik_ayarla(d):
    """Değeri 0-100 aralığına sınırlar ve Pico'ya gönderir."""
    durum["duty"] = max(0, min(100, int(d)))
    if not SIM:
        try: requests.get(f"{PICO}/duty?d={durum['duty']}", timeout=1.0)
        except Exception: pass

def veri_oku():
    if SIM: return dict(durum)
    try: return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception: return None

@ui.page("/")
def ana():
    ui.label("Aydınlatma Kontrolü").classes("text-h5")
    yuzde = ui.label("parlaklık: 0 %").classes("text-h4")
    ui.label("Parlaklık (%)").classes("text-caption")
    ui.slider(min=0, max=100, value=0,
              on_change=lambda e: (parlaklik_ayarla(e.value), yuzde.set_text(f"parlaklık: {int(e.value)} %")))
    with ui.row():
        ui.button("Kapat", on_click=lambda: (parlaklik_ayarla(0), yuzde.set_text("parlaklık: 0 %")))
        ui.button("Tam", on_click=lambda: (parlaklik_ayarla(100), yuzde.set_text("parlaklık: 100 %")))
    with ui.card():
        ui.label("Zaman programı").classes("text-subtitle2")
        saat = ui.time(value="20:00")
        seviye = ui.number("Parlaklık (%)", value=40, min=0, max=100)
        kayitlar = ui.log(max_lines=6).style("height:120px")
        ui.button("Programa ekle", icon="schedule",
                  on_click=lambda: (kayitlar.push(f"{saat.value} → %{seviye.value} parlaklık"),
                                    parlaklik_ayarla(seviye.value),
                                    yuzde.set_text(f"parlaklık: {int(seviye.value)} %")))

    def guncelle():
        v = veri_oku()
        if v is not None:
            yuzde.set_text(f"parlaklık: {v['duty']} %")

    ui.timer(3.0, guncelle, immediate=True)

import os
if os.environ.get("SELFTEST"):
    for _ in range(3): print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="Dimmer", port=8080, show=False, reload=False)

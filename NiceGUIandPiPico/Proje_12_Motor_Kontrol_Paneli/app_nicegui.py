# Proje 12: Motor Kontrol Paneli — NiceGUI arayüzü
import requests
from nicegui import ui

PICO = "http://192.168.1.50:8080"
SIM = True
durum = {"duty": 0, "yon": "dur"}

def komut(duty=None, yon=None):
    """Pico'ya PWM ve yön komutu gönderir."""
    if duty is not None: durum["duty"] = int(duty)
    if yon is not None: durum["yon"] = yon
    if not SIM:
        yol = f"{PICO}/pwm?d={durum['duty']}"
        if yon: yol += f"&yon={yon}"
        try: requests.get(yol, timeout=1.0)
        except Exception: pass

def veri_oku():
    if SIM:
        return dict(durum)
    try:
        return requests.get(f"{PICO}/data", timeout=1.0).json()
    except Exception:
        return None

@ui.page("/")
def ana():
    ui.label("Motor Kontrol Paneli").classes("text-h5")
    hiz_et = ui.label("hız: 0 %").classes("text-h4")
    durum_et = ui.label("yön: dur").classes("text-subtitle1")
    ui.label("Hız (%)").classes("text-caption")
    ui.slider(min=0, max=100, value=0,
              on_change=lambda e: (komut(duty=e.value), hiz_et.set_text(f"hız: {int(e.value)} %")))
    with ui.row():
        ui.button("İleri", icon="arrow_forward",
                  on_click=lambda: (komut(yon="ileri"), durum_et.set_text("yön: ileri")))
        ui.button("Geri", icon="arrow_back",
                  on_click=lambda: (komut(yon="geri"), durum_et.set_text("yön: geri")))
        ui.button("ACİL DUR", icon="pan_tool", color="negative",
                  on_click=lambda: (komut(duty=0, yon="dur"), hiz_et.set_text("hız: 0 %"),
                                    durum_et.set_text("yön: dur")))
    with ui.card():
        ui.label("Joystick (sürükleyin)").classes("text-caption")
        ui.joystick(on_move=lambda e: (komut(duty=min(100, abs(e.x) * 100)),
                                       hiz_et.set_text(f"hız: {int(min(100, abs(e.x) * 100))} %")))

    def guncelle():
        v = veri_oku()
        if v is not None:
            hiz_et.set_text(f"hız: {v['duty']} %")
            durum_et.set_text(f"yön: {v['yon']}")

    ui.timer(2.0, guncelle, immediate=True)

import os
if os.environ.get("SELFTEST"):
    for _ in range(3): print("veri:", veri_oku())
    raise SystemExit(0)

ui.run(title="Motor Paneli", port=8080, show=False, reload=False)

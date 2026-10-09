# Proje 19: Etiket / QR Üretici — NiceGUI arayüzü
import base64, io, requests
from nicegui import ui
try:
    import qrcode          # pip install qrcode pillow
except ImportError:
    qrcode = None

PICO = "http://192.168.1.50:8080"
SIM = True

def qr_veri_url(metin: str) -> str:
    """Metinden QR kod üretir ve base64 PNG veri adresi döndürür."""
    if qrcode is None:
        return ""
    img = qrcode.make(metin)
    tampon = io.BytesIO()
    img.save(tampon, format="PNG")
    return "data:image/png;base64," + base64.b64encode(tampon.getvalue()).decode()

def yaziciya_gonder(metin: str):
    if not SIM:
        try: requests.get(f"{PICO}/yaz?metin={metin.replace(' ', '%20').replace(chr(10), '%0A')}", timeout=3.0)
        except Exception: pass

@ui.page("/")
def ana():
    ui.label("Etiket / QR Üretici").classes("text-h5")
    malzeme = ui.input("Malzeme adı", value="Direnç 1k")
    raf = ui.input("Raf / kutu", value="A-12")
    barkod = ui.input("Barkod / stok no", value="8680001")
    onizleme = ui.image("").style("width:150px")

    def guncelle_onizleme():
        etiket = f"{malzeme.value}\nRaf: {raf.value}\nNo: {barkod.value}"
        onizleme.set_source(qr_veri_url(etiket) or "")

    for alan in (malzeme, raf, barkod):
        alan.on_value_change(lambda e: guncelle_onizleme())
    guncelle_onizleme()

    def yazdir():
        etiket = f"{malzeme.value}\nRaf: {raf.value}\nNo: {barkod.value}"
        yaziciya_gonder(etiket)
        ui.notify(f"Etiket gönderildi: {malzeme.value}", type="positive")

    ui.button("Etiketi yazdır", icon="print", on_click=yazdir)
    ui.label("QR kod Pico'ya bağlı termal yazıcıdan basılır; önizleme tarayıcıda üretilir.").classes("text-caption")

import os
if os.environ.get("SELFTEST"):
    print("qr veri adresi uzunluğu:", len(qr_veri_url("deneme")))
    raise SystemExit(0)

ui.run(title="Etiket Üretici", port=8080, show=False, reload=False)

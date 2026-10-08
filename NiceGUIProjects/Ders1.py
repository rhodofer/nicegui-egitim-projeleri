from nicegui import ui

# 1. Başlık ve Karşılama Metni
ui.label("NiceGUI ile İlk Web Arayüzüm").classes("text-h4 text-primary font-bold")
ui.label("Aşağıdaki butonları kullanarak reaktif sayaç sistemini test edebilirsiniz.").classes("text-gray-600")

# 2. Sayaç Değişkeni ve Gösterge Etiketi
sayac = 0
sayac_etiketi = ui.label(f"Mevcut Değer: {sayac}").classes("text-h5 text-bold my-4")

# 3. Buton Olay Fonksiyonları
def artir():
    global sayac
    sayac += 1
    sayac_etiketi.text = f"Mevcut Değer: {sayac}"
    ui.notify(f"Sayaç artırıldı: {sayac}", type="positive")

def sifirla():
    global sayac
    sayac = 0
    sayac_etiketi.text = f"Mevcut Değer: {sayac}"
    ui.notify("Sayaç sıfırlandı!", type="warning")

# 4. Butonlar (Yatay Dizilim İçin ui.row kullanımı)
with ui.row():
    ui.button("Artır (+1)", on_click=artir, icon="add").classes("bg-blue-600")
    ui.button("Sıfırla", on_click=sifirla, icon="refresh").classes("bg-red-600")
    # Kısa işlemler için lambda kullanımı örneği
    ui.button("Bilgi", on_click=lambda: ui.notify("Sistem hazır ve çalışıyor!", type="info"))

# 5. Sunucuyu Başlat (Koyu tema ve özel başlık ile)
ui.run(title="NiceGUI İlk Uygulama", port=8080, dark=False)
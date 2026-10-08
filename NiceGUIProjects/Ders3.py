from nicegui import ui

# Renk paleti tanımlama
ui.colors(primary='#2563eb', secondary='#0d9488', accent='#f59e0b', positive='#10b981', negative='#ef4444')

with ui.card().classes('w-full max-w-2xl mx-auto mt-6 p-6 shadow-lg rounded-xl border border-slate-200 bg-white'):
    ui.label('NiceGUI Seçim ve Yerleşim Paneli').classes('text-2xl font-bold text-slate-800 mb-1')
    ui.label('Chip Etiketleri, Row Yerleşimi, Toggle ve Radio Kontrolleri').classes('text-sm text-slate-500 mb-6')

    # 1. Row ve Chip Bileşenleri
    ui.label('1. Yatay Sıralama (Row) ve Etiketler (Chip)').classes('text-sm font-semibold text-slate-700 uppercase tracking-wider')
    with ui.row().classes('gap-2 mb-6 items-center flex-wrap'):
        ui.chip('Python', icon='code', color='blue-600', text_color='white')
        ui.chip('NiceGUI 2.0', icon='web', color='teal-600', text_color='white')
        ui.chip('Filtre: Aktif', icon='check_circle', selectable=True, on_click=lambda: ui.notify('Filtre durumu değişti'))
        ui.chip('Kaldırılabilir Etiket', icon='tag', removable=True, on_click=lambda: ui.notify('Etiket kapatıldı'))

    # 2. Toggle (Seçenek Değiştirici)
    ui.label('2. Çoklu Seçenek Butonu (Toggle)').classes('text-sm font-semibold text-slate-700 uppercase tracking-wider')
    with ui.row().classes('mb-6 items-center gap-4'):
        gorunum_toggle = ui.toggle(['Özet Rapor', 'Detaylı Tablo', 'Grafik Analiz'], value='Detaylı Tablo', 
            on_change=lambda e: ui.notify(f'Görünüm modu: {e.value}')
        ).props('spread rounded unelevated color=primary')

    # 3. Radio (Tekli Seçim Düğmeleri)
    ui.label('3. Radyo Buton Grubu (Radio)').classes('text-sm font-semibold text-slate-700 uppercase tracking-wider')
    with ui.row().classes('mb-6 items-center gap-6'):
        veri_kaynagi = ui.radio(['Canlı Saha Verisi', 'Simülatör Modu', 'Geçmiş Arşiv'], value='Canlı Saha Verisi',
            on_change=lambda e: ui.notify(f'Kaynak seçildi: {e.value}')
        ).props('inline color=teal')

    # 4. Canlı Durum Paneli (Reaktif Bağlama)
    with ui.column().classes('w-full bg-slate-50 p-4 rounded-lg border border-slate-200 gap-1'):
        ui.label('Anlık Seçim Durumu:').classes('text-xs font-bold text-slate-500 uppercase')
        ui.label().bind_text_from(gorunum_toggle, 'value', backward=lambda v: f'📊 Aktif Görünüm: {v}').classes('text-sm font-medium text-slate-800')
        ui.label().bind_text_from(veri_kaynagi, 'value', backward=lambda v: f'📡 Veri Kaynağı: {v}').classes('text-sm font-medium text-slate-800')

ui.run(title='NiceGUI Seçim Kontrolleri', port=8080)
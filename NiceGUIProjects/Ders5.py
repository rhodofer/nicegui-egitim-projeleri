from nicegui import ui

ui.colors(primary='#4f46e5', secondary='#06b6d4', accent='#f59e0b', positive='#10b981', negative='#ef4444')

with ui.card().classes('w-full max-w-3xl mx-auto my-6 p-6 shadow-xl rounded-2xl border border-slate-200 bg-white'):
    with ui.row().classes('items-center gap-3 mb-2'):
        ui.icon('settings_input_composite', size='md').classes('text-indigo-600')
        ui.label('Endüstriyel Cihaz & Kod Konfigürasyon Paneli').classes('text-2xl font-bold text-slate-800')
    ui.label('Gelişmiş Form Kontrolleri: Input, Number, Textarea, CodeMirror, Renk, Tarih ve Saat').classes('text-sm text-slate-500 mb-6')

    # 1. Cihaz Kimlik ve Sayısal Parametreler
    ui.label('1. Cihaz Kimliği ve Çalışma Gerilimi').classes('text-xs font-bold text-slate-500 uppercase tracking-wider')
    with ui.row().classes('w-full mb-4 items-center gap-4'):
        cihaz_adi = ui.input(
            label='Cihaz / İstasyon Tanımı',
            value='PLC-Gateway-Node-01',
            placeholder='Örn: Node-01',
            validation={'En az 4 karakter': lambda v: len(v) >= 4}
        ).classes('flex-1')

        cihaz_sifre = ui.input(
            label='Güvenlik PIN / Şifre',
            value='Admin#2026',
            password=True,
            password_toggle_button=True
        ).classes('flex-1')

        calisma_voltaji = ui.number(
            label='Çalışma Gerilimi',
            value=24.0,
            min=0.0,
            max=48.0,
            step=0.5,
            suffix=' V',
            format='%.1f'
        ).classes('w-40')

    # 2. Çok Satırlı Saha Açıklaması
    ui.label('2. Saha Bakım ve Kalibrasyon Raporu').classes('text-xs font-bold text-slate-500 uppercase tracking-wider')
    with ui.row().classes('w-full mb-4'):
        aciklama = ui.textarea(
            label='Bakım ve Konfigürasyon Notu',
            value='Hat 3 üzerindeki sıcaklık ve basınç sensörleri kontrol edildi. Modbus RTU haberleşmesi nominal seviyede devrede.',
            placeholder='Saha notlarını buraya giriniz...'
        ).classes('w-full').props('rows=3 outlined')

    # 3. Sözdizimi Vurgulamalı Kod Editörü (CodeMirror)
    ui.label('3. Telemetri Kancası (Python CodeMirror Editörü)').classes('text-xs font-bold text-slate-500 uppercase tracking-wider')
    with ui.column().classes('w-full mb-4 gap-1'):
        kod_metni = """def telemetry_hook(packet):
    # Sensör veri paketi filtreleme kancası
    temperature = packet.get('temp', 0.0)
    voltage = packet.get('volt', 24.0)
    return {'status': 'ONLINE', 'alert': temperature > 55.0}"""
        kod_editor = ui.codemirror(kod_metni, language='python').classes('w-full border border-slate-300 rounded-lg overflow-hidden shadow-sm')

    # 4. Tarih, Saat ve Renk Seçicileri
    ui.label('4. Bakım Zamanlaması ve Durum LED Rengi').classes('text-xs font-bold text-slate-500 uppercase tracking-wider')
    with ui.row().classes('w-full mb-6 items-center gap-4 flex-wrap'):
        with ui.input(label='Muayene Tarihi', value='2026-10-07').classes('w-48') as tarih_inp:
            with tarih_inp.add_slot('append'):
                ui.icon('event').classes('cursor-pointer text-slate-500').on('click', lambda: tarih_menu.open())
            with ui.menu() as tarih_menu:
                ui.date().bind_value(tarih_inp)

        with ui.input(label='Planlanan Saat', value='14:30').classes('w-36') as saat_inp:
            with saat_inp.add_slot('append'):
                ui.icon('access_time').classes('cursor-pointer text-slate-500').on('click', lambda: saat_menu.open())
            with ui.menu() as saat_menu:
                ui.time().bind_value(saat_inp)

        led_renk = ui.color_input(label='LED Renk Kodu', value='#10b981').classes('w-44')

    # 5. Aksiyon Butonu ve Canlı Dağıtım Özeti
    ozet_kutusu = ui.column().classes('w-full bg-slate-50 p-4 rounded-xl border border-slate-200 gap-2')
    with ozet_kutusu:
        ui.label('Kaydedilen Sistem Parametreleri:').classes('text-xs font-bold text-slate-500 uppercase')
        ozet_metin = ui.label(
            f'📡 Cihaz: {cihaz_adi.value} | ⚡ Gerilim: {calisma_voltaji.value} V | 📅 Tarih: {tarih_inp.value} {saat_inp.value} | 🟢 LED: {led_renk.value}'
        ).classes('text-sm font-semibold text-slate-800')

    def kaydet_ve_guncelle():
        ozet_metin.text = f'📡 Cihaz: {cihaz_adi.value} | ⚡ Gerilim: {calisma_voltaji.value} V | 📅 Tarih: {tarih_inp.value} {saat_inp.value} | 🟢 LED: {led_renk.value}'
        ui.notify('Konfigürasyon başarıyla kaydedildi ve dağıtıldı!', type='positive', icon='cloud_done')

    with ui.row().classes('w-full justify-end mt-4'):
        ui.button('Konfigürasyonu Kaydet & Dağıt', icon='save', on_click=kaydet_ve_guncelle).classes('bg-indigo-600 text-white shadow-md')

ui.run(title='NiceGUI Gelişmiş Form Paneli', port=8080)
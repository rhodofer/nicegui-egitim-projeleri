from nicegui import ui

ui.colors(primary='#0284c7', secondary='#0d9488', accent='#f59e0b', positive='#10b981', negative='#ef4444')

with ui.card().classes('w-full max-w-2xl mx-auto mt-6 p-6 shadow-lg rounded-xl border border-slate-200 bg-white'):
    ui.label('NiceGUI Form ve Kontrol Paneli').classes('text-2xl font-bold text-slate-800 mb-1')
    ui.label('Select (Açılır Liste), Checkbox, Switch ve Slider').classes('text-sm text-slate-500 mb-6')

    # 1. Açılır Liste (Select)
    ui.label('1. Açılır Liste Seçimi (ui.select)').classes('text-sm font-semibold text-slate-700 uppercase tracking-wider')
    with ui.row().classes('w-full mb-6 items-center gap-4'):
        hat_secimi = ui.select(
            options=['Hat 1 — Montaj İstasyonu', 'Hat 2 — CNC İşleme', 'Hat 3 — Paketleme'],
            value='Hat 1 — Montaj İstasyonu',
            label='Aktif Üretim Hattı'
        ).classes('w-72')

    # 2. Onay Kutuları (Checkbox)
    ui.label('2. Onay Kutuları (ui.checkbox)').classes('text-sm font-semibold text-slate-700 uppercase tracking-wider')
    with ui.row().classes('w-full mb-6 items-center gap-6 flex-wrap'):
        oto_kayit = ui.checkbox('Otomatik Veri Kaydı', value=True)
        sesli_uyari = ui.checkbox('Sesli Alarm Aktif', value=False)
        e_posta = ui.checkbox('Günlük PDF Gönder', value=True)

    # 3. Kaydırmalı Anahtar (Switch)
    ui.label('3. Durum Anahtarı (ui.switch)').classes('text-sm font-semibold text-slate-700 uppercase tracking-wider')
    with ui.row().classes('w-full mb-6 items-center gap-6'):
        canli_akisi = ui.switch('Canlı Telemetri Yayını', value=True).props('color=primary')
        gece_modu = ui.switch('Vardiya Gece Modu', value=False).props('color=secondary')

    # 4. Sayısal Kaydırıcı (Slider)
    ui.label('4. Değer Kaydırıcısı (ui.slider)').classes('text-sm font-semibold text-slate-700 uppercase tracking-wider')
    with ui.column().classes('w-full mb-6 gap-2'):
        with ui.row().classes('w-full items-center justify-between'):
            ui.label('Bant Hızı / Kapasite Limiti:').classes('text-sm text-slate-600')
            hiz_etiketi = ui.label('75 %').classes('text-sm font-bold text-sky-700')
        hiz_slider = ui.slider(min=0, max=100, value=75, step=5).props('label label-always color=sky-600')
        hiz_etiketi.bind_text_from(hiz_slider, 'value', backward=lambda v: f'{v} %')

    # 5. Dinamik Durum Özeti (Reaktif Bağlama)
    with ui.column().classes('w-full bg-slate-50 p-4 rounded-lg border border-slate-200 gap-1'):
        ui.label('Seçili Sistem Parametreleri:').classes('text-xs font-bold text-slate-500 uppercase')
        ui.label().bind_text_from(hat_secimi, 'value', backward=lambda v: f'📍 Seçili Hat: {v}').classes('text-sm font-medium text-slate-800')
        ui.label().bind_text_from(canli_akisi, 'value', backward=lambda v: f'⚡ Yayın Durumu: {"Aktif" if v else "Kapalı"}').classes('text-sm font-medium text-slate-800')
        ui.label().bind_text_from(hiz_slider, 'value', backward=lambda v: f'🎚️ Çalışma Hızı: %{v}').classes('text-sm font-medium text-slate-800')

ui.run(title='NiceGUI Form Kontrolleri', port=8080)
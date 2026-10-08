from nicegui import ui

# Renk paleti
ui.colors(primary='#1e40af', secondary='#0284c7', accent='#10b981', positive='#10b981', negative='#ef4444')

with ui.card().classes('w-full max-w-2xl mx-auto mt-6 p-6 shadow-lg rounded-xl border border-slate-200 bg-white'):
    ui.label('NiceGUI Buton & Kontrol Paneli').classes('text-2xl font-bold text-slate-800 mb-2')
    ui.label('Temel Butonlar, Buton Grupları, Dropdown ve FAB').classes('text-sm text-slate-500 mb-6')

    # 1. Standart ve İkonlu Butonlar
    ui.label('1. Standart ve İkonlu Butonlar').classes('text-sm font-semibold text-slate-700 uppercase tracking-wider')
    with ui.row().classes('gap-3 mb-6 items-center flex-wrap'):
        ui.button('Kaydet', icon='save', on_click=lambda: ui.notify('Veri kaydedildi!', type='positive')).classes('bg-blue-600 text-white')
        ui.button('İptal', icon='close', color='negative', on_click=lambda: ui.notify('İşlem iptal edildi.', type='negative'))
        ui.button('Dışa Aktar', icon='download', color='secondary').props('outline')
        ui.button(icon='favorite', color='red-5').props('flat round')

    # 2. Buton Grubu (Button Group)
    ui.label('2. Buton Grubu (Button Group)').classes('text-sm font-semibold text-slate-700 uppercase tracking-wider')
    with ui.row().classes('mb-6 items-center gap-4'):
        with ui.button_group().classes('shadow-sm'):
            ui.button('Günlük', on_click=lambda: ui.notify('Görünüm: Günlük'))
            ui.button('Haftalık', on_click=lambda: ui.notify('Görünüm: Haftalık'))
            ui.button('Aylık', on_click=lambda: ui.notify('Görünüm: Aylık'))

    # 3. Açılır Menü Butonu (Dropdown Button)
    ui.label('3. Açılır Menü Butonu (Dropdown Button)').classes('text-sm font-semibold text-slate-700 uppercase tracking-wider')
    with ui.row().classes('mb-6 items-center gap-4'):
        with ui.dropdown_button('Rapor Türü Seç', icon='assessment', color='primary'):
            ui.item('PDF Özeti İndir', on_click=lambda: ui.notify('PDF hazırlanıyor...'))
            ui.item('Excel Tablosu', on_click=lambda: ui.notify('Excel oluşturuldu.'))
            ui.separator()
            ui.item('JSON Ham Veri', on_click=lambda: ui.notify('JSON aktarıldı.'))

    ui.label('Etkileşim Bildirimi: Son tıklama bildirim kutusunda sağ altta gösterilir.').classes('text-xs text-slate-400 italic')

# 4. FAB (Floating Action Button)
with ui.fab(icon='settings', color='amber-8').classes('fixed bottom-6 right-6'):
    ui.fab_action(icon='person_add', on_click=lambda: ui.notify('Yeni kullanıcı eklendi')).props('color=blue')
    ui.fab_action(icon='share', on_click=lambda: ui.notify('Bağlantı paylaşıldı')).props('color=green')
    ui.fab_action(icon='delete', on_click=lambda: ui.notify('Çöp kutusuna taşındı')).props('color=red')

ui.run(title='NiceGUI Buton Kontrolleri', port=8080)
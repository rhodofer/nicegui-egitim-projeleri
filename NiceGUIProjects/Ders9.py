"""
NiceGUI Ders 9: Bindings — Reaktif Veri Bağlama
Kapsamlı Uygulama: bind_value, bind_text_from, bind_visibility_from, bind_enabled_from
"""
from nicegui import ui

ui.page_title('NiceGUI Ders 9 — Veri Bağlama (Bindings)')

# Reaktif Veri Modeli Sözlüğü
sistem_durumu = {
    'istasyon_adi': 'Hat-01 Reaktörü',
    'hedef_sicaklik': 45.0,
    'guvenlik_kilidi': True,
    'otomatik_pilot': False
}

with ui.column().classes('w-full max-w-4xl mx-auto p-6 gap-6'):
    # Başlık Kartı
    with ui.card().classes('w-full p-5 shadow-sm border border-slate-200'):
        with ui.row().classes('w-full items-center justify-between'):
            with ui.row().classes('items-center gap-3'):
                ui.icon('sync_alt', size='md').classes('text-blue-600')
                with ui.column().classes('gap-0'):
                    ui.label('Ders 9: Reaktif Veri Bağlama ve Senkronizasyon').classes('text-2xl font-bold text-slate-800')
                    ui.label('Çift yönlü ve tek yönlü veri bağları ile anlık UI senkronizasyonu').classes('text-xs text-slate-500')
            ui.badge('Two-Way Binding', color='blue').props('outline')

    # 1. Çift Yönlü Değer Bağı (bind_value)
    ui.label('1. Çift Yönlü Kontrol Bağı (Slider <-> Number <-> Model)').classes('text-sm font-bold uppercase tracking-wider text-slate-500')
    with ui.card().classes('w-full p-4 shadow-sm border'):
        with ui.row().classes('w-full items-center gap-6'):
            slider = ui.slider(min=20, max=100, step=0.5).classes('flex-1')
            sayi = ui.number(min=20, max=100, step=0.5, suffix=' °C').classes('w-32')
            
            # Slider ile Sayı alanını çift yönlü birbirine bağla
            slider.bind_value(sistem_durumu, 'hedef_sicaklik')
            sayi.bind_value(sistem_durumu, 'hedef_sicaklik')

        with ui.row().classes('w-full items-center justify-between mt-3 pt-3 border-t text-sm'):
            # Dönüştürücülü (backward) canlı etiket
            ui.label().bind_text_from(
                sistem_durumu, 'hedef_sicaklik',
                backward=lambda t: f'🔥 Ayarlanan Sıcaklık: {t:.1f} °C (Kritik Eşik: 80 °C)'
            ).classes('font-bold text-blue-700')

            ui.label().bind_text_from(
                sistem_durumu, 'hedef_sicaklik',
                backward=lambda t: '⚠️ DİKKAT: Yüksek Isı!' if t >= 80 else '✅ Normal Aralık'
            ).classes('font-semibold')

    # 2. Yetki & Etkinlik Bağı (bind_enabled_from)
    ui.label('2. Şartlı Etkinlik ve Güvenlik Kilidi (bind_enabled_from)').classes('text-sm font-bold uppercase tracking-wider text-slate-500 mt-2')
    with ui.card().classes('w-full p-4 shadow-sm border'):
        with ui.row().classes('w-full items-center justify-between'):
            kilit = ui.switch('Güvenlik Kilidini Aç').bind_value(sistem_durumu, 'guvenlik_kilidi')
            
            # Buton yalnızca kilit açıkken tıklanabilir
            acil_btn = ui.button('Reaktörü Başlat', icon='play_arrow', color='positive')
            acil_btn.bind_enabled_from(sistem_durumu, 'guvenlik_kilidi')
            acil_btn.on('click', lambda: ui.notify('Reaktör başarıyla ateşlendi!', type='positive'))

    # 3. Görünürlük Bağı (bind_visibility_from)
    ui.label('3. Dinamik Görünürlük (bind_visibility_from)').classes('text-sm font-bold uppercase tracking-wider text-slate-500 mt-2')
    with ui.card().classes('w-full p-4 shadow-sm border'):
        oto_switch = ui.switch('Otopilot Modunu Aktif Et').bind_value(sistem_durumu, 'otomatik_pilot')
        
        # Bu bilgi paneli yalnızca otomatik pilot aktifken görünür
        with ui.card().classes('w-full bg-blue-50 border border-blue-200 p-4 mt-3').bind_visibility_from(sistem_durumu, 'otomatik_pilot'):
            ui.label('🤖 Otopilot Sistemi Devrede').classes('font-bold text-blue-900')
            ui.label('Tüm valf ve sıcaklık regülatörleri yapay zeka algoritması tarafından otomatik yönetiliyor.').classes('text-xs text-blue-700')

ui.run(port=8089, reload=False)
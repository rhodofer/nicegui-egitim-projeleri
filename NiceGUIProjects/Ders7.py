"""
NiceGUI Ders 7: Yerleşim ve Düzen (Layout Architecture)
Kapsamlı Uygulama: ui.row, ui.column, ui.card, ui.grid, ui.expansion, ui.tabs, ui.splitter
"""
from nicegui import ui

ui.page_title('NiceGUI Ders 7 — Yerleşim ve Düzen')

with ui.column().classes('w-full max-w-5xl mx-auto p-6 gap-6'):
    # 1. Başlık Kartı
    with ui.card().classes('w-full p-5 shadow-sm border border-slate-200 bg-white'):
        with ui.row().classes('w-full items-center justify-between'):
            with ui.row().classes('items-center gap-3'):
                ui.icon('dashboard_customize', size='md').classes('text-blue-600')
                with ui.column().classes('gap-0'):
                    ui.label('Ders 7: Modern Sayfa Düzeni ve Konteyner Mimarisi').classes('text-xl font-bold text-slate-800')
                    ui.label('Flexbox, Grid, Sekmeler, Akordiyon ve Splitter ile temiz arayüzler').classes('text-xs text-slate-500')
            ui.badge('Flexbox & Grid', color='blue').props('outline')

    # 2. Üst İki Sütun: Grid & Kart Hiyerarşisi
    ui.label('1. Çok Sütunlu Kart Izgarası (ui.grid & ui.card)').classes('text-sm font-bold text-slate-600 uppercase tracking-wider')
    with ui.grid(columns=3).classes('w-full gap-4'):
        with ui.card().classes('p-4 border-t-4 border-emerald-500 shadow-sm'):
            with ui.row().classes('items-center justify-between'):
                ui.label('Üretim Hattı A').classes('font-bold text-slate-800')
                ui.icon('precision_manufacturing', size='sm').classes('text-emerald-500')
            ui.label('Durum: Aktif (98.4%)').classes('text-xs text-slate-500 mt-2')
            ui.linear_progress(0.98, show_value=False).props('color=positive rounded')

        with ui.card().classes('p-4 border-t-4 border-amber-500 shadow-sm'):
            with ui.row().classes('items-center justify-between'):
                ui.label('Montaj Hattı B').classes('font-bold text-slate-800')
                ui.icon('build_circle', size='sm').classes('text-amber-500')
            ui.label('Durum: Bakımda (42.0%)').classes('text-xs text-slate-500 mt-2')
            ui.linear_progress(0.42, show_value=False).props('color=warning rounded')

        with ui.card().classes('p-4 border-t-4 border-indigo-500 shadow-sm'):
            with ui.row().classes('items-center justify-between'):
                ui.label('Test İstasyonu C').classes('font-bold text-slate-800')
                ui.icon('verified', size='sm').classes('text-indigo-500')
            ui.label('Durum: Testte (76.5%)').classes('text-xs text-slate-500 mt-2')
            ui.linear_progress(0.76, show_value=False).props('color=primary rounded')

    # 3. İki Bölmeli Splitter (Sürükleyerek Boyutlandırılan Alan)
    ui.label('2. Dinamik Bölücü ve Sekmeler (ui.splitter & ui.tabs)').classes('text-sm font-bold text-slate-600 uppercase tracking-wider mt-2')
    with ui.card().classes('w-full p-0 overflow-hidden shadow-sm border border-slate-200'):
        with ui.splitter(value=30).classes('w-full h-64') as splitter:
            with splitter.before:
                with ui.column().classes('p-4 gap-2 bg-slate-50 h-full border-r border-slate-200'):
                    ui.label('Sol Kontrol Paneli').classes('font-bold text-xs uppercase text-slate-500')
                    ui.button('Sistem Günlükleri', icon='list_alt').props('flat align=left').classes('w-full text-slate-700')
                    ui.button('Hata Takip', icon='bug_report').props('flat align=left').classes('w-full text-slate-700')
                    ui.button('Güvenlik Ayarları', icon='security').props('flat align=left').classes('w-full text-slate-700')

            with splitter.after:
                with ui.column().classes('p-4 gap-3 h-full'):
                    with ui.tabs().classes('w-full') as tabs:
                        tab1 = ui.tab('Genel Bakış', icon='dashboard')
                        tab2 = ui.tab('Ağ & Veri', icon='router')
                    
                    with ui.tab_panels(tabs, value=tab1).classes('w-full flex-1'):
                        with ui.tab_panel(tab1):
                            ui.label('Genel Sistem Metrikleri').classes('font-bold text-slate-700')
                            ui.label('Tüm düğümler kesintisiz 24 saattir online. Bellek kullanımı %34 seviyesinde.').classes('text-sm text-slate-500')
                        with ui.tab_panel(tab2):
                            ui.label('Ağ Trafiği ve Gateway').classes('font-bold text-slate-700')
                            ui.label('Gelen paket hızı: 1420 pkt/sn | Gecikme süresi: 12ms.').classes('text-sm text-slate-500')

    # 4. Akordiyon (ui.expansion) ile Yer Kazandıran Detaylar
    with ui.expansion('Gelişmiş Yerleşim Parametreleri & CSS Notları', icon='tune').classes('w-full bg-slate-50 border rounded-lg shadow-sm'):
        with ui.column().classes('p-4 gap-2 text-sm text-slate-600'):
            ui.label('• ui.row() yatay (flex-row), ui.column() dikey (flex-col) akış kurar.')
            ui.label('• gap-4, items-center ve justify-between sınıfları aralık ve hizalama sağlar.')
            ui.label('• ui.splitter() iki alan arasında kullanıcı tarafından taşınabilen sürgü yerleştirir.')

ui.run(port=8089, reload=False)
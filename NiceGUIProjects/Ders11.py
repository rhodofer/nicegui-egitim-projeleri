"""
NiceGUI Ders 11: Veri Öğeleri (Data Elements, Tables, Tree & Gauges)
Kapsamlı Uygulama: ui.table, ui.aggrid, ui.tree, ui.circular_progress, ui.knob
"""
from nicegui import ui

ui.page_title('NiceGUI Ders 11 — Veri Öğeleri')

with ui.column().classes('w-full max-w-5xl mx-auto p-6 gap-6'):
    # Başlık Kartı
    with ui.card().classes('w-full p-5 shadow-sm border border-slate-200'):
        with ui.row().classes('w-full items-center justify-between'):
            with ui.row().classes('items-center gap-3'):
                ui.icon('table_chart', size='md').classes('text-blue-600')
                with ui.column().classes('gap-0'):
                    ui.label('Ders 11: Veri Tabloları, Hiyerarşik Ağaç ve İlerleme Göstergeleri').classes('text-2xl font-bold text-slate-800')
                    ui.label('ui.table, ui.aggrid, ui.tree, dinamik progress ve knob bileşenleri').classes('text-xs text-slate-500')
            ui.badge('Data & Tables', color='blue').props('outline')

    # 1. Metrik Kartları ve İlerleme Göstergeleri
    ui.label('1. Canlı Göstergeler ve İlerleme Metrikleri').classes('text-sm font-bold uppercase tracking-wider text-slate-500')
    with ui.row().classes('w-full gap-4 items-stretch'):
        with ui.card().classes('flex-1 p-4 items-center text-center shadow-sm border'):
            ui.label('CPU Yükü').classes('text-xs font-bold uppercase text-slate-500')
            ui.circular_progress(0.68, show_value=True, color='primary').classes('my-2')
            ui.label('4 Çekirdek Aktif').classes('text-xs text-slate-400')

        with ui.card().classes('flex-1 p-4 items-center text-center shadow-sm border'):
            ui.label('Bellek Kullanımı').classes('text-xs font-bold uppercase text-slate-500')
            ui.circular_progress(0.42, show_value=True, color='positive').classes('my-2')
            ui.label('6.8 GB / 16 GB').classes('text-xs text-slate-400')

        with ui.card().classes('flex-1 p-4 items-center text-center shadow-sm border'):
            ui.label('Hedef Sıcaklık Regülatörü').classes('text-xs font-bold uppercase text-slate-500')
            knob = ui.knob(value=45, min=0, max=100, show_value=True, color='amber').classes('my-1')
            ui.label('Ayar Düğmesi (Knob)').classes('text-xs text-slate-400')

    # 2. İki Sütun: Tablo & Hiyerarşik Ağaç
    ui.label('2. İnteraktif Tablo ve Hiyerarşik Ağaç (ui.table & ui.tree)').classes('text-sm font-bold uppercase tracking-wider text-slate-500 mt-2')
    with ui.row().classes('w-full gap-6 items-start'):
        # ui.table alanı
        with ui.column().classes('flex-1'):
            columns = [
                {'name': 'id', 'label': 'Cihaz Kodu', 'field': 'id', 'align': 'left', 'sortable': True},
                {'name': 'konum', 'label': 'Konum', 'field': 'konum', 'align': 'left', 'sortable': True},
                {'name': 'gerilim', 'label': 'Gerilim (V)', 'field': 'gerilim', 'sortable': True},
                {'name': 'durum', 'label': 'Durum', 'field': 'durum', 'align': 'center'}
            ]
            rows = [
                {'id': 'PLC-01', 'konum': 'Hat A - Giriş', 'gerilim': 24.2, 'durum': 'Çalışıyor'},
                {'id': 'PLC-02', 'konum': 'Hat A - Fırın', 'gerilim': 23.8, 'durum': 'Çalışıyor'},
                {'id': 'PLC-03', 'konum': 'Hat B - Paketleme', 'gerilim': 24.0, 'durum': 'Uyarı'},
                {'id': 'PLC-04', 'konum': 'Hat C - Depo', 'gerilim': 22.1, 'durum': 'Bakımda'}
            ]
            
            secim_etiketi = ui.label('Seçilen Cihaz: Yok').classes('text-xs font-bold text-blue-700 mb-1')
            
            def satir_secildi(e):
                secilen = e.selection
                if secilen:
                    secim_etiketi.text = f"🎯 Seçilen Cihaz: {secilen[0]['id']} ({secilen[0]['konum']})"
                else:
                    secim_etiketi.text = 'Seçilen Cihaz: Yok'

            tablo = ui.table(columns=columns, rows=rows, row_key='id', selection='single', on_select=satir_secildi)
            tablo.classes('w-full shadow-sm rounded-lg border')

        # ui.tree alanı
        with ui.card().classes('w-72 p-4 shadow-sm border'):
            ui.label('Tesis Hiyerarşisi (ui.tree)').classes('font-bold text-slate-700 border-b pb-2 mb-2')
            nodes = [
                {
                    'id': 'tesis', 'label': 'Fabrika Genel',
                    'children': [
                        {
                            'id': 'hat_a', 'label': 'Üretim Hattı A',
                            'children': [{'id': 'plc1', 'label': 'PLC-01'}, {'id': 'plc2', 'label': 'PLC-02'}]
                        },
                        {
                            'id': 'hat_b', 'label': 'Montaj Hattı B',
                            'children': [{'id': 'plc3', 'label': 'PLC-03'}]
                        }
                    ]
                }
            ]
            ui.tree(nodes, label_key='label', on_select=lambda e: ui.notify(f"Ağaç düğümü: {e.value}"))

ui.run(port=8089, reload=False)
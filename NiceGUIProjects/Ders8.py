"""
NiceGUI Ders 8: Biçimlendirme, Renk Paleti ve Tema (Styling, Classes & Dark Mode)
Kapsamlı Uygulama: ui.colors, ui.dark_mode, .classes(), .style(), .props()
"""
from nicegui import ui

# 1. Özel Kurumsal Renk Paleti Tanımlama
ui.colors(
    primary='#0284c7',    # Canlı Gök Mavisi
    secondary='#6366f1',  # İndigo Mor
    accent='#f59e0b',     # Kehribar Sarı
    positive='#10b981',   # Zümrüt Yeşil
    negative='#ef4444',   # Kırmızı
    info='#06b6d4'        # Camgöbeği
)

ui.page_title('NiceGUI Ders 8 — Biçimlendirme & Stil')

# Karanlık Mod Nesnesi
dark = ui.dark_mode()

with ui.column().classes('w-full max-w-4xl mx-auto p-6 gap-6'):
    # Başlık ve Tema Değiştirici Kartı
    with ui.card().classes('w-full p-5 shadow-sm border border-slate-200'):
        with ui.row().classes('w-full items-center justify-between'):
            with ui.row().classes('items-center gap-3'):
                ui.icon('palette', size='md').classes('text-primary')
                with ui.column().classes('gap-0'):
                    ui.label('Ders 8: Biçimlendirme, Renk Paletleri & Tema').classes('text-2xl font-bold')
                    ui.label('Tailwind sınıfları, Quasar props ve dinamik Dark Mode').classes('text-xs text-slate-500')
            
            # Canlı Karanlık Mod Anahtarı
            with ui.row().classes('items-center gap-2'):
                ui.icon('light_mode', size='xs').classes('text-amber-500')
                ui.switch('Karanlık Mod').bind_value_to(dark, 'value')
                ui.icon('dark_mode', size='xs').classes('text-indigo-500')

    # 1. Classes, Style ve Props Karşılaştırma Alanı
    ui.label('1. Biçimlendirme Yöntemleri (.classes, .style, .props)').classes('text-sm font-bold uppercase tracking-wider text-slate-500')
    with ui.row().classes('w-full gap-4 items-stretch'):
        # .classes örneği
        with ui.card().classes('flex-1 p-4 shadow-sm border'):
            ui.label('.classes()').classes('font-bold text-primary border-b pb-2 mb-2')
            ui.label('Tailwind CSS Gücü').classes('text-lg font-bold text-emerald-600')
            ui.label('Yazı boyutu, dolgu (padding), kenarlık ve yuvarlatma sınıfları doğrudan eklenir.').classes('text-xs text-slate-500')
            ui.button('Tailwind Butonu').classes('bg-emerald-600 text-white rounded-full mt-3 w-full shadow-md')

        # .style örneği
        with ui.card().classes('flex-1 p-4 shadow-sm border'):
            ui.label('.style()').classes('font-bold text-primary border-b pb-2 mb-2')
            ui.label('Doğrudan CSS Kuralı').style('color: #9333ea; font-size: 17px; font-weight: 700; letter-spacing: 0.05em;')
            ui.label('Özel gradyanlar, piksel bazlı gölgeler veya dinamik renk kodları atanır.').classes('text-xs text-slate-500')
            ui.button('Gradyanlı Buton').style('background: linear-gradient(135deg, #9333ea, #c026d3); color: white; border-radius: 8px; margin-top: 12px; width: 100%;')

        # .props örneği
        with ui.card().classes('flex-1 p-4 shadow-sm border'):
            ui.label('.props()').classes('font-bold text-primary border-b pb-2 mb-2')
            ui.label('Quasar Bileşen Nitelikleri').classes('text-lg font-bold text-sky-600')
            ui.label('outlined, rounded, unelevated, glossy gibi hazır framework özellikleri eklenir.').classes('text-xs text-slate-500')
            ui.button('Quasar Outlined').props('outline color=primary icon=auto_awesome').classes('w-full mt-3')

    # 2. Kurumsal Renk Paleti Gösterimi
    ui.label('2. ui.colors() ile Tanımlanan Renk Paleti').classes('text-sm font-bold uppercase tracking-wider text-slate-500 mt-2')
    with ui.card().classes('w-full p-4 shadow-sm border'):
        with ui.row().classes('w-full gap-3 justify-between items-center'):
            ui.badge('Primary', color='primary').classes('p-2 text-sm')
            ui.badge('Secondary', color='secondary').classes('p-2 text-sm')
            ui.badge('Positive', color='positive').classes('p-2 text-sm')
            ui.badge('Warning / Accent', color='accent').classes('p-2 text-sm')
            ui.badge('Negative', color='negative').classes('p-2 text-sm')
            ui.badge('Info', color='info').classes('p-2 text-sm')

ui.run(port=8089, reload=False)
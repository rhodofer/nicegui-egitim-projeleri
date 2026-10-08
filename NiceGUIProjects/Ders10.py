"""
NiceGUI Ders 10: Görsel ve İşitsel Medya (AudioVisual Elements)
Kapsamlı Uygulama: ui.image, ui.interactive_image, ui.video, ui.audio, ui.scene, ui.log
"""
from nicegui import ui

ui.page_title('NiceGUI Ders 10 — Görsel ve İşitsel Medya')

with ui.column().classes('w-full max-w-5xl mx-auto p-6 gap-6'):
    # Başlık Kartı
    with ui.card().classes('w-full p-5 shadow-sm border border-slate-200'):
        with ui.row().classes('w-full items-center justify-between'):
            with ui.row().classes('items-center gap-3'):
                ui.icon('perm_media', size='md').classes('text-blue-600')
                with ui.column().classes('gap-0'):
                    ui.label('Ders 10: Görsel, İşitsel ve 3D Medya Bileşenleri').classes('text-2xl font-bold text-slate-800')
                    ui.label('İnteraktif resimler, video/ses oynatıcıları, WebGL 3B sahneler ve canlı log').classes('text-xs text-slate-500')
            ui.badge('Multimedia & 3D', color='blue').props('outline')

    # 1. İnteraktif Görüntü İşleme & Koordinat Yakalama
    ui.label('1. İnteraktif Resim ve Koordinat Tespiti (ui.interactive_image)').classes('text-sm font-bold uppercase tracking-wider text-slate-500')
    with ui.card().classes('w-full p-4 shadow-sm border'):
        with ui.row().classes('w-full gap-6 items-start'):
            # Resim alanı
            with ui.column().classes('flex-1'):
                koordinat_etiketi = ui.label('Tıklanan Nokta: Resim üzerine tıklayın').classes('text-sm font-bold text-blue-700 mb-2')
                
                def resim_tiklandi(e):
                    x = getattr(e, 'image_x', 0)
                    y = getattr(e, 'image_y', 0)
                    koordinat_etiketi.text = f'🎯 Tıklanan Koordinat: X={x:.1f}px, Y={y:.1f}px'
                    log_kutusu.push(f'[TESPİT] Hedef işaretlendi: ({x:.1f}, {y:.1f})')

                img = ui.interactive_image('https://picsum.photos/id/1060/600/320', on_mouse=resim_tiklandi).classes('rounded-lg shadow w-full')

            # Canlı Akış Günlüğü
            with ui.column().classes('w-72'):
                ui.label('Canlı Olay Günlüğü (ui.log)').classes('text-xs font-bold uppercase text-slate-500')
                log_kutusu = ui.log(max_lines=6).classes('w-full h-44 bg-slate-900 text-emerald-400 p-3 rounded font-mono text-xs')
                log_kutusu.push('[SİSTEM] Görüntü analiz modülü hazır.')

    # 2. İki Sütun: Video & 3B WebGL Sahnesi (ui.video & ui.scene)
    ui.label('2. Video Akışı ve 3B Sahne Modelleme (ui.video & ui.scene)').classes('text-sm font-bold uppercase tracking-wider text-slate-500 mt-2')
    with ui.row().classes('w-full gap-6 items-stretch'):
        # Video Kartı
        with ui.card().classes('flex-1 p-4 shadow-sm border'):
            ui.label('HTML5 Video Oynatıcı (ui.video)').classes('font-bold text-slate-700 border-b pb-2 mb-2')
            ui.video('https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4').classes('w-full rounded shadow')
            
            # Ses Oynatıcı Eki
            ui.label('Ses Oynatıcı (ui.audio)').classes('text-xs font-bold text-slate-500 mt-3 mb-1 uppercase')
            ui.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3').classes('w-full')

        # 3B WebGL Kartı
        with ui.card().classes('flex-1 p-4 shadow-sm border'):
            ui.label('Gerçek Zamanlı 3B Sahne (ui.scene)').classes('font-bold text-slate-700 border-b pb-2 mb-2')
            with ui.scene(width=420, height=220).classes('w-full bg-slate-950 rounded shadow') as sahne:
                sahne.spot_light(distance=100, intensity=0.8).move(0, 0, 10)
                sahne.sphere().material('#0ea5e9').move(-1.5, 0, 0)
                sahne.box(1.5, 1.5, 1.5).material('#10b981').move(1.5, 0, 0)
            ui.label('Fareyle sürükleyerek 3B nesneleri döndürebilir ve yakınlaştırabilirsiniz.').classes('text-xs text-slate-400 text-center mt-2')

ui.run(port=8089, reload=False)
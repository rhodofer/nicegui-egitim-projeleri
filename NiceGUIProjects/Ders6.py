"""
NiceGUI Ders 6: Metin Öğeleri (Text Elements)
Kapsamlı Uygulama: ui.label, ui.link, ui.markdown, ui.html, ui.chat_message
"""
from nicegui import ui
from datetime import datetime

# Sayfa başlık ve genel düzeni
ui.page_title('NiceGUI Ders 6 — Metin Öğeleri')

with ui.column().classes('w-full max-w-4xl mx-auto p-6 gap-6'):
    # 1. Başlık ve Tipografi (ui.label)
    with ui.card().classes('w-full shadow-md border-l-4 border-blue-600 p-5'):
        ui.label('Ders 6: Metin ve İletişim Bileşenleri').classes('text-2xl font-bold text-blue-900')
        ui.label('NiceGUI ile zengin metinler, bağlantılar ve sohbet arayüzleri oluşturma').classes('text-sm text-gray-500 mb-2')
        
        with ui.row().classes('items-center gap-3 mt-2'):
            ui.label('Düz Etiket (Default)').classes('text-base')
            ui.label('Kalın & Renkli').classes('font-semibold text-emerald-600')
            ui.label('Küçük Bilgi').classes('text-xs text-gray-400 uppercase tracking-wider')
            # ui.link örneği
            ui.link('NiceGUI Resmi Dokümantasyon ↗', 'https://nicegui.io', new_tab=True).classes('text-blue-600 hover:underline font-medium text-sm ml-auto')

    # 2. İki Sütunlu Düzen: Markdown & HTML
    with ui.row().classes('w-full gap-6 items-stretch'):
        # Markdown Alanı
        with ui.card().classes('flex-1 shadow-sm border border-gray-200 p-4'):
            ui.label('Markdown Desteği (ui.markdown)').classes('font-bold text-gray-700 border-b pb-2 mb-3')
            md_content = '''
### Canlı Sistem Notları
- **Durum:** Servisler aktif ve yanıt veriyor.
- **İpucu:** `ui.markdown` sözdizimini doğrudan render eder.

> *"NiceGUI, Python geliştiricileri için web geliştirmeyi hızlandırır."*
            '''
            ui.markdown(md_content).classes('text-sm')

        # Özel HTML Alanı
        with ui.card().classes('flex-1 shadow-sm border border-gray-200 p-4'):
            ui.label('Özel HTML Alanı (ui.html)').classes('font-bold text-gray-700 border-b pb-2 mb-3')
            ui.html('''
                <div style="background: linear-gradient(135deg, #eff6ff, #dbeafe); padding: 14px; border-radius: 8px; border: 1px dashed #3b82f6;">
                    <span style="display:inline-block; font-size: 11px; font-weight:700; color:#1d4ed8; text-transform:uppercase; letter-spacing:0.05em;">Özel Rozet</span>
                    <h4 style="margin:6px 0 4px 0; color:#1e3a8a; font-size:15px; font-weight:700;">HTML İle Tam Stil Denetimi</h4>
                    <p style="margin:0; font-size:12.5px; color:#334155;">Doğrudan CSS ve özel HTML etiketlerini arayüze ekleyin.</p>
                </div>
            ''')

    # 3. Sohbet & İletişim Akışı (ui.chat_message)
    with ui.card().classes('w-full shadow-sm border border-gray-200 p-5'):
        ui.label('Destek & Mesajlaşma Akışı (ui.chat_message)').classes('font-bold text-gray-800 border-b pb-2 mb-4')
        
        # Mesajların listeleneceği kapsayıcı
        chat_container = ui.column().classes('w-full gap-2 mb-4')

        with chat_container:
            ui.chat_message('Sistem başlatıldı. Sensör verileri dinleniyor.', 
                            name='Sistem Botu', stamp='10:45', avatar='https://robohash.org/bot?set=set1')
            ui.chat_message('Harika, sıcaklık eşik değerini 40°C olarak günceller misin?', 
                            name='Mühendis Ali', stamp='10:47', sent=True)
            ui.chat_message('Eşik değeri 40°C olarak tanımlandı. Her şey normal.', 
                            name='Sistem Botu', stamp='10:48', avatar='https://robohash.org/bot?set=set1')

        # Yeni mesaj gönderme girişi
        with ui.row().classes('w-full items-center gap-3 pt-3 border-t'):
            msg_input = ui.input(placeholder='Mesajınızı yazın...').classes('flex-1')
            
            def send_msg():
                val = msg_input.value.strip() if msg_input.value else ''
                if not val:
                    ui.notify('Lütfen bir mesaj yazın!', color='warning')
                    return
                now_str = datetime.now().strftime('%H:%M')
                with chat_container:
                    ui.chat_message(val, name='Operatör', stamp=now_str, sent=True)
                msg_input.value = ''
                ui.notify('Mesaj eklendi!', color='positive')

            ui.button('Gönder', on_click=send_msg, icon='send').props('unelevated color=primary')

ui.run(port=8089, reload=False)
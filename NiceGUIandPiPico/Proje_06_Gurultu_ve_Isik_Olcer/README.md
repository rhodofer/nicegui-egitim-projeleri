# Proje 6 — Gürültü ve Işık Ölçer

## 🎯 Projenin Amacı
Mikrofon modülü ve LDR ile ortam sesi ve ışık seviyesini ölçüp eşik aşımında uyarı vermek.

## 🔌 Donanım ve Malzeme Listesi
| Malzeme | Adet | Yaklaşık fiyat / temin |
| --- | --- | --- |
| Raspberry Pi Pico W (veya Pico 2 W) | 1 | fiyat teyit edilmeli (Robotistan / Direnc.net) |
| Mikrofon amplifikatör modülü (MAX4466/MAX9814) | 1 | ≈ 80–150 TL (teyit edilmeli) |
| LDR + 10 kΩ direnç | 1 | ≈ 10 TL |
| Jumper kablo | 1 | ≈ 30 TL |

## 🌐 Veri Akışı ve Mimari
Pico iki ADC kanalını okuyup 0–100 bağıl seviyeye ölçekler ve yayınlar; arayüz iki çubuk gösterge çizer, eşik üstü ses olaylarını günlüğe yazar.

## 🛠️ Nasıl Çalıştırılır?

### 1. Raspberry Pi Pico W (Donanım Katmanı)
1. Pico W cihazınızı USB ile bilgisayara bağlayın ve Thonny IDE'yi açın.
2. `main_pico.py` dosyasındaki `SSID` ve `SIFRE` değişkenlerini kendi kablosuz ağınıza göre düzenleyin.
3. Kodu Pico içerisine `main.py` adıyla kaydedin ve çalıştırın.
4. Thonny konsolunda görünen IP adresini (Örn: `192.168.1.50`) not edin.

### 2. Bilgisayar / Sunucu (NiceGUI Web Arayüzü)
1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install nicegui requests
   ```
2. `app_nicegui.py` dosyasındaki `PICO = "http://<pico-ip>:8080"` adresini yukarıdaki IP ile güncelleyin.
3. Donanım bağlı değilse `SIM = True` bırakarak simülasyon verileriyle test edebilirsiniz. Gerçek cihaz için `SIM = False` yapın.
4. Terminalden uygulamayı başlatın:
   ```bash
   python app_nicegui.py
   ```
5. Tarayıcınızda otomatik olarak açılan `http://localhost:8080` adresinden kontrol panelini kullanın.

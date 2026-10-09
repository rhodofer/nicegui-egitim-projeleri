# Proje 3 — Sera İklim Kontrolü

## 🎯 Projenin Amacı
Sera sıcaklık, nem ve ışık değerlerini izleyip eşik aşıldığında fanı otomatik devreye almak; arayüzden eşik ayarlamak.

## 🔌 Donanım ve Malzeme Listesi
| Malzeme | Adet | Yaklaşık fiyat / temin |
| --- | --- | --- |
| Raspberry Pi Pico W (veya Pico 2 W) | 1 | fiyat teyit edilmeli (Robotistan / Direnc.net) |
| DHT22 | 1 | ≈ 88–106 TL |
| LDR + 10 kΩ direnç | 1 | ≈ 10 TL |
| 1 kanal röle modülü (fan) | 1 | ≈ 75–98 TL |
| 12 V fan | 1 | ≈ 100–200 TL (teyit edilmeli) |

## 🌐 Veri Akışı ve Mimari
Pico üç büyüklüğü ölçüp /data ile yayınlar; arayüz eşikleri tutar ve gerektiğinde /fan?d=1 komutunu gönderir. Otomatik karar hem Pico hem arayüz tarafında kurulabilir.

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

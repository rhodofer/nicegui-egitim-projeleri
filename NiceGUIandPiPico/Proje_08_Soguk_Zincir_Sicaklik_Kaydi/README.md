# Proje 8 — Soğuk Zincir Sıcaklık Kaydı (DS18B20)

## 🎯 Projenin Amacı
DS18B20 ile sıcaklığı kaydedip eşik aşımını raporlamak; CSV tabanlı veri kaydını ve tablo gösterimini öğrenmek.

## 🔌 Donanım ve Malzeme Listesi
| Malzeme | Adet | Yaklaşık fiyat / temin |
| --- | --- | --- |
| Raspberry Pi Pico W (veya Pico 2 W) | 1 | fiyat teyit edilmeli (Robotistan / Direnc.net) |
| DS18B20 su geçirmez sıcaklık sensörü | 1 | ≈ 40–47 TL |
| 4,7 kΩ direnç (pull-up) | 1 | ≈ 1 TL |
| Kablo/klemens | 1 | ≈ 20 TL |

## 🌐 Veri Akışı ve Mimari
Pico sıcaklığı okur, Pico&#8217;nun iç dosya sistemine log.csv olarak yazar ve /data ile son değeri, /log ile son 10 satırı yayınlar; arayüz tablo ve eşik uyarısı gösterir.

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

# Proje 18 — Envanter Paneli (Barkod + Ağırlık HX711)

## 🎯 Projenin Amacı
Laboratuvar malzemelerini barkod okuyucu ve yük hücresi ile takip etmek; düşük stok uyarısı üretmek.

## 🔌 Donanım ve Malzeme Listesi
| Malzeme | Adet | Yaklaşık fiyat / temin |
| --- | --- | --- |
| Raspberry Pi Pico W (veya Pico 2 W) | 1 | fiyat teyit edilmeli (Robotistan / Direnc.net) |
| Barkod okuyucu (UART/TTL çıkışlı) | 1 | ≈ 500–900 TL (teyit edilmeli) |
| HX711 + yük hücresi (load cell) | 1 | ≈ 78–150 TL + hücre ≈ 100–300 TL |
| Jumper kablo | 1 | ≈ 30 TL |

## 🌐 Veri Akışı ve Mimari
Pico barkod okuyucudan gelen satırı ve yük hücresinden ağırlığı okur, /data ile yayınlar; arayüz envanter tablosunu günceller ve arama yapılır.

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

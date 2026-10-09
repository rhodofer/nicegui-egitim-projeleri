# Proje 10 — Solar Şarj İzleyici (INA219)

## 🎯 Projenin Amacı
Panel gerilimi ve şarj akımını ölçüp gücü ve batarya doluluk oranını (SOC) izlemek.

## 🔌 Donanım ve Malzeme Listesi
| Malzeme | Adet | Yaklaşık fiyat / temin |
| --- | --- | --- |
| Raspberry Pi Pico W (veya Pico 2 W) | 1 | fiyat teyit edilmeli (Robotistan / Direnc.net) |
| Gerilim bölücü dirençler (ör. 100 kΩ + 20 kΩ) | 1 | ≈ 10 TL |
| Şönt direnç veya Hall akım sensörü (ACS712) | 1 | ≈ 100–200 TL (teyit edilmeli) |
| Solar panel + 12 V akü (mevcut sistem) | 1 | — |

## 🌐 Veri Akışı ve Mimari
Pico panel gerilimini bölücüden, akımı şönt/Hall sensöründen okur; gücü ve SOC tahminini yayınlar; arayüz üç ölçüm ve dairesel doluluk göstergesi çizer.

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

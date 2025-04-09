# Geleceğin Aynası (Mirror of the Future)
## ENGLISH ON THE BOTTOM

Geleceğin Aynası, kullanıcıların metin girişlerini yapay zeka ile geliştirerek 20 yıl sonraki halini tahmin eden ve görselleştiren bir web uygulamasıdır.

## Özellikler

- **Metin Geliştirme**: Girdilerinizi detaylı gelecek tahminlerine dönüştürür
- **Görsel Üretimi**: Geliştirilmiş metin açıklamalarına dayalı görseller oluşturur
- **Ses Tanıma**: Tarayıcı tabanlı konuşma tanıma özelliği ile sesli girişleri destekler
- **Modern Arayüz**: Sezgisel ve kullanıcı dostu web arayüzü

## Gereksinimler

- Python 3.8 veya daha yeni sürüm
- pip (Python paket yöneticisi)
- Git (kurulum için)
- En az 4GB RAM (AI modelleri için)
- Disk alanı: minimum 2GB (AI modelleri için)
- Modern web tarayıcı (Chrome, Firefox, Edge veya Safari)

## Kurulum

### Windows için Kurulum

1. Python'u [Python resmi sitesinden](https://www.python.org/downloads/windows/) indirin ve kurun
   - Kurulum sırasında "Add Python to PATH" seçeneğini işaretleyin

2. Repoyu klonlayın:
   ```
   git clone https://github.com/EmreYesilkaya/FUTURE-MIRROR.git
   cd gelecegin-aynasi
   ```

3. Sanal ortam oluşturun ve etkinleştirin:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

4. Gerekli paketleri yükleyin:
   ```
   pip install -r requirements.txt
   ```
   Not: Bu adım modelleri indireceği için biraz zaman alabilir (yaklaşık 5-10 dakika)

5. Çevresel değişkenleri ayarlayın (.env dosyası):
   ```
   copy .env.example .env
   ```
   Not: Opsiyonel olarak, .env dosyasını düzenleyip kendi API anahtarlarınızı ekleyebilirsiniz

6. Uygulamayı başlatın:
   ```
   python app.py
   ```

8. Tarayıcınızda şu adresi açın: `http://127.0.0.1:5001`

### Mac için Kurulum

1. Homebrew kurulu değilse, terminal üzerinden kurun:
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Python kurulumu:
   ```
   brew install python
   ```

3. Repoyu klonlayın:
   ```
   git clone https://github.com/KULLANICIADINIZ/gelecegin-aynasi.git
   cd gelecegin-aynasi
   ```

4. Sanal ortam oluşturun ve etkinleştirin:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

5. Gerekli paketleri yükleyin:
   ```
   pip install -r requirements.txt
   ```
   Not: Bu adım modelleri indireceği için biraz zaman alabilir (yaklaşık 5-10 dakika)

6. Çevresel değişkenleri ayarlayın (.env dosyası):
   ```
   cp .env.example .env
   ```
   Not: Opsiyonel olarak, .env dosyasını düzenleyip kendi API anahtarlarınızı ekleyebilirsiniz

7. Uygulamayı başlatın:
   ```
   python app.py
   ```

8. Tarayıcınızda şu adresi açın: `http://127.0.0.1:5001`

### Linux için Kurulum

1. Terminal üzerinden Python ve Git kurun:
   ```
   sudo apt update
   sudo apt install python3 python3-pip python3-venv git
   ```

2. Repoyu klonlayın:
   ```
   git clone https://github.com/KULLANICIADINIZ/gelecegin-aynasi.git
   cd gelecegin-aynasi
   ```

3. Sanal ortam oluşturun ve etkinleştirin:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Gerekli paketleri yükleyin:
   ```
   pip install -r requirements.txt
   ```
   Not: Bu adım modelleri indireceği için biraz zaman alabilir (yaklaşık 5-10 dakika)

5. Çevresel değişkenleri ayarlayın (.env dosyası):
   ```
   cp .env.example .env
   ```
   Not: Opsiyonel olarak, .env dosyasını düzenleyip kendi API anahtarlarınızı ekleyebilirsiniz

6. Uygulamayı başlatın:
   ```
   python app.py
   ```

7. Tarayıcınızda şu adresi açın: `http://127.0.0.1:5001`

## Kullanım

1. Web arayüzünde, metin kutusuna geleceğini görmek istediğiniz nesne veya kavramı yazın (örneğin "akıllı telefon", "araba", "şehir").

2. Metni yazabilir veya "Speak to Record" butonunu kullanarak sesli olarak girebilirsiniz:
   - Mikrofon erişimine izin vermeniz gerekebilir
   - Kayıt sırasında buton kırmızı renkte yanıp söner
   - Konuşmanız tamamlandığında, tanınan metin otomatik olarak metin kutusuna yerleştirilir

3. "Show the Future" butonuna tıklayın.

4. İlk kullanımda, AI modelleri indirildiği için işlem biraz zaman alabilir (1-3 dakika). Sonraki kullanımlarda daha hızlı olacaktır.

5. Sonuçlar sayfada gösterilecektir:
   - Girdiğinizin geliştirilmiş bir gelecek açıklaması
   - Bu açıklamaya dayalı bir görsel

## Komut Satırı Kullanımı

Uygulamayı komut satırı arayüzü üzerinden de kullanabilirsiniz:

```
python cli.py --text "geleceğini görmek istediğiniz nesne"
```

veya etkileşimli mod:

```
python cli.py
```

## Proje Yapısı

- `app.py`: Ana Flask web uygulaması
- `text_enhancer.py`: Metin geliştirme modeli (TinyLlama entegrasyonu)
- `image_generator.py`: Görsel üretim modülü (Stable Diffusion)
- `cli.py`: Komut satırı arayüzü
- `templates/`: HTML şablonları
- `outputs/`: Oluşturulan görsellerin kaydedildiği klasör

## Sorun Giderme

- **Modeller indirilemiyorsa**: Internet bağlantınızı kontrol edin veya VPN kullanın
- **"CUDA out of memory" hatası**: GPU belleği yetersizse, `image_generator.py` dosyasındaki görsel boyutlarını ve adımları azaltın
- **Konuşma tanıma çalışmıyorsa**: Tarayıcınızın mikrofon erişimine izin verdiğinden emin olun
- **Uygulama çok yavaşsa**: CPU modunda çalışıyor olabilir, daha hızlı bir bilgisayar veya GPU kullanın

## Notlar

- İlk kullanımda, yaklaşık 1.5GB'lık AI modelleri indirilecektir
- Görsel üretimi CPU'da çalışırsa yavaş olabilir, GPU kullanımı önerilir (NVIDIA GPU tercih edilir)
- Web arayüzündeki konuşma tanıma, tarayıcının WebSpeech API'sini kullanır ve internet bağlantısı gerektirir

## Lisans

MIT

---

# English Instructions

## Mirror of the Future

This project is an AI-powered web application that enhances user text inputs to predict and visualize how objects or concepts might look 20 years in the future.

## Features

- **Text Enhancement**: Transforms your inputs into detailed future predictions
- **Image Generation**: Creates visuals based on enhanced text descriptions
- **Voice Recognition**: Browser-based speech recognition for voice inputs
- **Modern Interface**: Intuitive and user-friendly web interface

## Installation

### Requirements

- Python 3.8 or newer
- pip (Python package manager)
- Git (for installation)
- Minimum 4GB RAM (for AI models)
- Disk space: minimum 2GB (for AI models)
- Modern web browser (Chrome, Firefox, Edge, or Safari)

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/YOURUSERNAME/gelecegin-aynasi.git
   cd gelecegin-aynasi
   ```

2. Create and activate a virtual environment:
   - Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```
   Note: This step may take some time (approximately 5-10 minutes) as it downloads AI models

4. Set up environment variables (.env file):
   - Windows:
     ```
     copy .env.example .env
     ```
   - Mac/Linux:
     ```
     cp .env.example .env
     ```
   Note: Optionally, you can edit the .env file to add your own API keys

5. Start the application:
   ```
   python app.py
   ```

6. Open your browser and navigate to: `http://127.0.0.1:5001`

## Troubleshooting

- **Models fail to download**: Check your internet connection or use a VPN
- **"CUDA out of memory" error**: If GPU memory is insufficient, reduce image dimensions and steps in `image_generator.py`
- **Speech recognition not working**: Ensure your browser has permission to access the microphone
- **Application is too slow**: It might be running in CPU mode; use a faster computer or GPU

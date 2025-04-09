#!/usr/bin/env python3
import argparse
import os
from text_enhancer import enhance_text
from image_generator import generate_image
# Import speech recognition only if the module is available
try:
    from speech_recognizer import recognize_speech
except ImportError:
    def recognize_speech(audio_file_path):
        print(f"Speech recognition module not found.")
        return None
from PIL import Image
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description='Geleceği Gösteren Ayna - Komut Satırı Arayüzü')
    parser.add_argument('--text', type=str, help='Geleceğini görmek istediğiniz nesne veya kavram')
    parser.add_argument('--audio', type=str, help='Ses dosyası yolu (.wav)')
    parser.add_argument('--output', type=str, default='output', help='Çıktı dosya ismi (uzantısız)')
    
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    os.makedirs('outputs', exist_ok=True)
    
    if not args.text and not args.audio:
        print("Lütfen bir metin girin veya ses dosyası belirtin!")
        text = input("Geleceğini görmek istediğiniz nesne veya kavram: ")
    else:
        if args.audio:
            print(f"Ses dosyası işleniyor: {args.audio}")
            text = recognize_speech(args.audio)
            if not text:
                print("Ses tanıma başarısız. Lütfen bir metin girin.")
                text = input("Geleceğini görmek istediğiniz nesne veya kavram: ")
        else:
            text = args.text
    
    print(f"\nGirdiğiniz: {text}")
    print("\nGeleceğe bakılıyor...")
    
    # Enhance the text
    enhanced_text = enhance_text(text)
    print(f"\nGeleceğin Görünümü:\n{enhanced_text}")
    
    # Generate image
    print("\nGörsel oluşturuluyor...")
    image_path = generate_image(enhanced_text)
    
    # Save results
    output_base = f"outputs/{args.output}"
    
    with open(f"{output_base}.txt", "w", encoding="utf-8") as f:
        f.write(f"Orijinal: {text}\n\n")
        f.write(f"Gelecek: {enhanced_text}")
    
    print(f"\nSonuçlar şu dosyalara kaydedildi:")
    print(f"Görsel: {image_path}")
    print(f"Metin: {output_base}.txt")
    
    # Open the image
    try:
        img = Image.open(image_path)
        img.show()
    except Exception as e:
        print(f"Görsel gösterilirken hata oluştu: {e}")

if __name__ == "__main__":
    main()
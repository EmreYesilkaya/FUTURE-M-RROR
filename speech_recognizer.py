import speech_recognition as sr

def recognize_speech(audio_file_path):
    """
    Python 3.13 uyumluluğu sorunu nedeniyle basitleştirilmiş ses tanıma fonksiyonu
    
    Args:
        audio_file_path (str): Path to the audio file
        
    Returns:
        str: Recognized text from the audio file (dummy response)
    """
    print(f"Ses dosyası alındı: {audio_file_path}")
    print("Not: Python 3.13 ses tanıma sorunu nedeniyle gerçek tanıma yapılamadı.")
    
    # Gerçek bir SpeechRecognition kullanımı yerine sadece bir dummy değer döndür
    return "örnek girdi tanımı"
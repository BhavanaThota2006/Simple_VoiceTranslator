import speech_recognition as sr
from deep_translator import GoogleTranslator
import pyttsx3
import sounddevice as sd
from scipy.io.wavfile import write
import tempfile
import os

def record_audio(filename, duration=5, fs=44100):
    import numpy as np
    from scipy.io.wavfile import write

    print("🎤 Speak now...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()

    # Convert float32 audio to int16 PCM format
    audio_int16 = np.int16(audio * 32767)
    write(filename, fs, audio_int16)


def listen_microphone():
    recognizer = sr.Recognizer()
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        filename = temp_file.name
    record_audio(filename)
    
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    os.remove(filename)
    
    try:
        text = recognizer.recognize_google(audio)
        print("📝 You said:", text)
        return text
    except sr.UnknownValueError:
        print("❌ Sorry, could not understand.")
        return None
    except sr.RequestError:
        print("⚠️ API request failed.")
        return None

def translate_text(text, dest_language='fr'):
    try:
        translation = GoogleTranslator(source='auto', target=dest_language).translate(text)
        print(f"🌍 Translated ({dest_language}):", translation)
        return translation
    except Exception as e:
        print("⚠️ Translation error:", e)
        return None

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def main():
    print("🔊 Real-Time Audio Translator (Python 3.13.3 Compatible)")
    print("Supported languages (ISO codes): fr (French), hi (Hindi), es (Spanish), de (German), ta (Tamil), etc.")
    
    target_lang = input("🌐 Enter target language code (e.g., 'fr'): ").strip().lower()

    text = listen_microphone()
    if text:
        translated = translate_text(text, dest_language=target_lang)
        if translated:
            speak_text(translated)

if __name__ == "__main__":
    main()

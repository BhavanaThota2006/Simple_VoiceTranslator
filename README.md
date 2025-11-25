**Real-Time Audio Translator**
A Python 3.13.3 Compatible Speech-to-Text → Translation → Text-to-Speech Pipeline
This project lets you speak through your microphone, automatically transcribes your speech, translates it into any language supported by Google Translate, and finally speaks the translated output using text-to-speech.
Perfect for beginners experimenting with Speech Recognition, Deep Translator, Audio Recording, and TTS in Python.

**Features**
✔️ Record audio using your microphone
✔️ Convert speech to text (Google Speech Recognition)
✔️ Translate text to any supported language
✔️ Speak translated text using pyttsx3
✔️ Works fully offline except the speech recognition API
✔️ Python 3.13.3 compatible

**Project Structure**
    │── app.py
    │── README.md

**How It Works**
User speaks → audio gets recorded
SpeechRecognition converts audio → text
Deep Translator translates text
pyttsx3 speaks out the translated output

**Supported Languages**
Enter any valid ISO language code:
Language	Code
French	  fr
Hindi    	hi
Spanish	  es
German	  de
Tamil    	ta
Italian	  it
Japanese	ja
Telugu	  te
…and many more.

**Usage**
Run the program: python app.py

You will see:
🔊 Real-Time Audio Translator (Python 3.13.3 Compatible)
Supported languages (ISO codes): fr (French), hi (Hindi), es (Spanish), de (German), ta (Tamil), etc.
🌐 Enter target language code (e.g., 'fr'):

**License**
This project is open-source under the MIT License.

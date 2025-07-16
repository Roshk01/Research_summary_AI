from gtts import gTTS
import os

def text_to_audio_light(text, filename="output.mp3"):
    tts = gTTS(text)
    filepath = os.path.join("audio", filename)
    os.makedirs("audio", exist_ok=True)
    tts.save(filepath)
    return filepath

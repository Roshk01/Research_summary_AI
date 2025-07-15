import pyttsx3
import os

def text_to_audio_light(text, filename="summary_audio.mp3", output_dir="output_audio"):
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    engine = pyttsx3.init()
    engine.setProperty('rate', 160)       # Adjust speed (optional)
    engine.setProperty('volume', 1.0)     # Volume (0.0 to 1.0)

    engine.save_to_file(text, output_path)
    engine.runAndWait()
    return output_path
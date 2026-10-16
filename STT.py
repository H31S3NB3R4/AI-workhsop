
import speech_recognition as sr

recognizer = sr.Recognizer()

try:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("LISTENING.....YOU MAY SPEAK")

        audio_data = recognizer.listen(
            source, timeout=3, phrase_time_limit=15
        )
        text = recognizer.recognize_google(audio_data)
        print(f"Transcription: {text}")

except Exception as e:
    print("Error:", e)

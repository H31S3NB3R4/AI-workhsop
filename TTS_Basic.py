from gtts import gTTS
import os

text="Hello all,blah blah blah"
tts=gTTS(text=text,lang="en")
tts.save("speech.wav")
import streamlit as st 
from gtts import gTTS
from io import BytesIO

st.set_page_config(page_title="TEXT TO SPEECH",page_icon="<|")

st.title("TEXT TO SPEECH")

text= st.text_area("ENTER YOUR TEXT:",height=150)

languages={
    "English":"en",
    "Hindi":"hi"

    
}
lang_name=st.selectbox("Language:",list(languages.keys()))
slow=st.checkbox("Speak slowly")

if st.button("convert to speech"):
    if not text.strip():
        st.warning("please enter some text first")
    else:
        with st.spinner("GENERATING AUDIO"):
            try:
                tts=gTTS(text=text, lang=languages[lang_name],slow=slow)
                audio=BytesIO()
                tts.write_to_fp(audio)
                audio.seek(0)
                st.audio(audio, format="audio/mp3")
                st.download_button(
                    label="Dowload MP3",

                    data=audio,
                    file_name="speech.mp3",
                    mime="audio/mp3"
                )
            except Exception as e:
                st.error(f"Something went wrong: {e}")
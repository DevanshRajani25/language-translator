from deep_translator import GoogleTranslator
import streamlit as st

st.title("Language Translator")

languages = GoogleTranslator().get_supported_languages()
user_input = st.text_input("Enter sentence/word to translate:")
dest_lang = st.selectbox("Select your destination language:", languages)

if st.button("Translate"):
    translated_text = GoogleTranslator(source='auto', target=dest_lang).translate(user_input)
    st.write(f"Translation: {translated_text}")

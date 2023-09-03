import streamlit as st
from utils.wav2mp3 import wav2mp3
from contents.expander import body as expander_body


st.set_page_config(page_title="wav2mp3 Translator", page_icon="🎶")
st.title("🎶 wav2mp3 Translator")
with st.expander("What is this?"):
    st.markdown(expander_body, unsafe_allow_html=False)

st.sidebar.header("🎛️ オプション設定")
with st.sidebar:
    bitrate = st.radio(
        "出力ビットレート[bps]", ["128k", "160k", "192k", "256k", "320k"], index=2
    )


upload_file = st.file_uploader("wav形式のファイルをアップロードしてください", type=".wav")
translate_button = st.button("変換する ➠")

if translate_button and not upload_file:
    st.info("wav形式のファイルをアップロードしてください")

if upload_file and translate_button:
    with st.spinner("変換中..."):
        audio_bytes = upload_file.read()
        filename = upload_file.name

        audio_mp3 = wav2mp3(wav_data=audio_bytes, bitrate=bitrate)
        st.audio(audio_mp3, format="audio/ogg")

        btn = st.download_button(
            label="Download as mp3",
            data=audio_mp3,
            file_name=filename.replace("wav", "mp3"),
            mime="audio/mp3",
        )

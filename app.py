import streamlit as st
import os

st.set_page_config(page_title="Music Vault", page_icon="🎵")

st.title("🎵 My Personal Music Vault")
st.markdown("---")

# Scan the music folder
music_folder = "music/raw"
files = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]

if not files:
    st.info("No music found. Run sync.py first!")
else:
    for song in sorted(files):
        with st.expander(f"▶️ {song}"):
            st.audio(os.path.join(music_folder, song))
            st.caption("Location: " + os.path.join(music_folder, song))
import streamlit as st
import requests

st.set_page_config(page_title="🎭 Emotion Detector", layout="centered")
st.title("🎭 Emotion Detector 3000")
st.markdown("Type your feeling and let the AI guess your vibe!")

# Emotion media (same as before)
emotion_gifs = {
    "joy": "https://media.giphy.com/media/yoJC2A59OCZHs1LXvW/giphy.gif",
    "sadness": "https://media.giphy.com/media/ROF8OQvDmxytW/giphy.gif",
    "anger": "https://media.giphy.com/media/l3vR9O2qfKAGTjCo0/giphy.gif",
    "neutral": "https://media.giphy.com/media/3og0IPxMM0erATueVW/giphy.gif"
}
emotion_music = {
    "joy": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "sadness": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3",
    "anger": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
    "neutral": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-12.mp3"
}

# Input
user_input = st.text_area("What's on your mind?", placeholder="E.g., I feel like dancing in the rain...")

if st.button("🔮 Analyze My Mood") and user_input.strip():
    try:
        # 🔁 Change this to your **public FastAPI URL** after deployment (for now keep localhost for testing)
        backend_url = "http://127.0.0.1:8000/predict"

        response = requests.post(backend_url, json={"text": user_input})
        result = response.json()

        label = result["emotion"]
        confidence = result["confidence"]

        st.success(f"🎯 Emotion: **{label.upper()}**\n🧠 Confidence: **{confidence}**")
        st.image(emotion_gifs.get(label.lower(), emotion_gifs["neutral"]), caption=f"{label.capitalize()} GIF")
        st.audio(emotion_music.get(label.lower(), emotion_music["neutral"]))
    except Exception as e:
        st.error("Something went wrong! Make sure the FastAPI backend is running and accessible.")

import streamlit as st
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch
import numpy as np
from pathlib import Path

# Load model and tokenizer
MODEL_PATH = "distilbert-base-uncased"  # or any fine-tuned public model
tokenizer = DistilBertTokenizer.from_pretrained(MODEL_PATH)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)

model.eval()

# Emotion labels
emotion_labels = [
    "admiration", "amusement", "anger", "annoyance", "approval", "caring",
    "confusion", "curiosity", "desire", "disappointment", "disapproval", "disgust",
    "embarrassment", "excitement", "fear", "gratitude", "grief", "joy", "love",
    "nervousness", "optimism", "pride", "realization", "relief", "remorse",
    "sadness", "surprise", "neutral"
]

# GIF and Music (simplified for demo)
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

# Streamlit UI
st.set_page_config(page_title="🎭 Emotion Detector", layout="centered")
st.title("🎭 Emotion Detector 3000")
st.markdown("Type your feeling and let the AI guess your vibe!")

user_input = st.text_area("What's on your mind?", placeholder="E.g., I feel like dancing in the rain...")

if st.button("🔮 Analyze My Mood") and user_input.strip():
    inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=1)
    top_pred = torch.argmax(probs, dim=1).item()
    emotion = emotion_labels[top_pred]
    confidence = float(probs[0][top_pred]) * 100

    st.success(f"🎯 Emotion: **{emotion.upper()}**\n🧠 Confidence: **{confidence:.2f}%**")
    st.image(emotion_gifs.get(emotion, emotion_gifs["neutral"]), caption=f"{emotion.capitalize()} GIF")

    st.audio(emotion_music.get(emotion, emotion_music["neutral"]))


import streamlit as st
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch
import numpy as np

st.set_page_config(page_title="🎭 Emotion Detector", layout="centered")
st.title("🎭 Emotion Detector 3000")
st.markdown("Type your feeling and let the AI guess your vibe!")

# Load pretrained emotion model from Hugging Face
MODEL_PATH = "bhadresh-savani/distilbert-base-uncased-emotion"


@st.cache_resource
def load_model():
    tokenizer = DistilBertTokenizer.from_pretrained(MODEL_PATH)
    model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
    model.eval()
    return tokenizer, model

tokenizer, model = load_model()
id2label = model.config.id2label

# Limited demo assets (only 4 categories for now)
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

user_input = st.text_area("What's on your mind?", placeholder="E.g., I feel like dancing in the rain...")

if st.button("🔮 Analyze My Mood") and user_input.strip():
    inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=1).cpu()
    top_pred = torch.argmax(probs.cpu(), dim=1).item()
    label = model.config.id2label[top_pred]
    confidence = float(probs[0][top_pred]) * 100

    st.success(f"🎯 Emotion: **{label.upper()}**\n🧠 Confidence: **{confidence:.2f}%**")
    st.image(emotion_gifs.get(label.lower(), emotion_gifs["neutral"]), caption=f"{label.capitalize()} GIF")
    st.audio(emotion_music.get(label.lower(), emotion_music["neutral"]))


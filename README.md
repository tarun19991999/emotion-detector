# 🎭 Emotion Detector 3000

An AI-powered full-stack web application that detects the emotional tone of any input text using a transformer-based NLP model (DistilBERT). The app provides visual feedback through GIFs and music tracks tailored to the detected emotion — all served through a sleek modern UI.

---

## 💡 Project Overview

The goal of this project is to classify the emotional content of a sentence into one of 28 emotions using a fine-tuned DistilBERT model. It is built using FastAPI for the backend, and vanilla HTML/CSS/JS for the frontend.

The project demonstrates:
- A user-friendly interface for submitting text
- A REST API that loads a pretrained transformer model
- NLP-based classification with real-time visualization (GIFs, audio)

---

## 🛠️ Tech Stack

| Layer         | Tools / Frameworks                |
|---------------|----------------------------------|
| Frontend      | HTML, CSS (Dark Theme), JavaScript |
| Backend       | FastAPI, Python, Pydantic        |
| Model         | Hugging Face Transformers (DistilBERT) |
| ML Framework  | PyTorch                          |
| Animation     | Particles.js (background effect) |

---


### 🧠 Features

- 🤖 Emotion prediction using a fine-tuned DistilBERT model
- 🎭 28 emotion classes (joy, sadness, anger, surprise, etc.)
- 🌐 FastAPI REST API backend
- 💡 Modern HTML/CSS/JS frontend
- 🎞️ Emotion-based GIFs
- 🎵 Emotion-based music
- 🔒 Confidence percentage displayed for predictions

---

### 🚀 How to Run

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Run the FastAPI backend**:
```bash
python -m uvicorn backend.main:app --reload
```

3. **Open the frontend**:  
Double-click `index.html` or serve using:
```bash
python -m http.server
http://localhost:8000/
```

4. **Use the app**:
- Type a sentence (e.g., _"I’m so excited!"_)
- Click “🔮 Analyze My Mood”
- See emotion, confidence, GIF, and hear a song

---

### 📁 Project Structure

```

├── backend/
│   ├── main.py
│   └── emotion-bert/
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
├── requirements.txt
├── README.md

```




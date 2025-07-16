# Research Paper Summarizer & Podcast Generator

This app fetches research papers from arXiv, summarizes them using transformers, classifies them by topic, and generates podcast-style audio.

---

## Features

- Search research papers from arXiv
- Classify summaries into topics
- Summarize papers using a transformer model
- Generate audio from summaries using gTTS
- Dockerized for one-command deployment
- Test_agents.ipynb includes all the examples for the agents and it's acceptable input format

---

## Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/research-summarizer.git
cd research-summarizer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
````

---

## Docker Setup (Recommended)

```bash
# 1. Build Docker image
docker build -t summarizer-app .

# 2. Run the container
docker run -p 8501:8501 summarizer-app
```

Visit: [http://localhost:8501](http://localhost:8501)

---

## 🎥 Guided Video

https://github.com/user-attachments/assets/c11146b0-6c7c-491d-8751-59d40775884a

https://github.com/user-attachments/assets/80357f76-3249-4f7a-95b1-0e7e2e2a8592

---

## Project Structure

```
.
├── app.py
├── agents/
│   ├── search_agent.py
│   ├── classification.py
│   ├── synthesis_agent.py
│   ├── audio_agent.py
│   ├── preprocess_agent.py
|   └── summary_agent.py
├── requirements.txt
├── Dockerfile
└── README.md
```


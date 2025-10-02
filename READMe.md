# 🚀 Day 1: AI Text Generator

This is my **Day 1 Project** for my **30 Days of Generative AI** portfolio.

## 📌 Project Overview
- Built with **Hugging Face Transformers (GPT-2)** + **Streamlit**
- Dockerized for easy deployment
- Generates text from any given prompt

## ▶ How to Run Locally
```bash
# Clone project
git clone <your-repo>
cd day1-text-generator

# Build docker image
docker build -t day1-ai .

# Run container
docker run -p 8501:8501 day1-ai

import streamlit as st
from transformers import pipeline

# Load text generation pipeline
generator = pipeline("text-generation")

st.set_page_config(page_title="Day 1 - Text Generator", page_icon="🚀")
st.title("🚀 Day 1: AI Text Generator")
st.write("Part of my 30 Days of Generative AI Journey")

# User input
prompt = st.text_area("Enter a prompt:", "kamkuha mo si lebron james")

if st.button("Generate Text"):
    with st.spinner("Generating..."):
        output = generator(prompt, max_length=50, num_return_sequences=1)
        st.success("✨ Generated Text")
        st.write(output[0]['generated_text'])

import streamlit as st
from transformers import pipeline
import os
from dotenv import load_dotenv

load_dotenv()
# Set your Hugging Face API token

HF_API_TOKEN = os.environ["HF_API_TOKEN"] 

# Page title
st.set_page_config(page_title='🦜🔗 Text Summarization App')
st.title('🦜🔗 Text Summarization App')

# Text input
txt_input = st.text_area('Enter your text', '', height=200)

@st.cache_resource
def load_summarizer():
    """Load summarization pipeline"""
    return pipeline("summarization", model="facebook/bart-large-cnn", token=HF_API_TOKEN)

def generate_response(txt):
    if not txt.strip():
        return "Please enter some text to summarize."
    
    summarizer = load_summarizer()
    
    # Handle long texts by splitting
    max_chunk = 1024
    if len(txt) > max_chunk:
        # Split into chunks
        words = txt.split()
        chunks = []
        current_chunk = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) < max_chunk:
                current_chunk.append(word)
                current_length += len(word) + 1
            else:
                chunks.append(" ".join(current_chunk))
                current_chunk = [word]
                current_length = len(word)
        
        if current_chunk:
            chunks.append(" ".join(current_chunk))
        
        # Summarize each chunk
        summaries = []
        for chunk in chunks:
            if len(chunk) > 100:  # Only summarize substantial chunks
                summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
                summaries.append(summary[0]['summary_text'])
        
        return " ".join(summaries)
    else:
        # Summarize directly for shorter texts
        summary = summarizer(txt, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']

# Form to accept user's text input for summarization
result = []
with st.form('summarize_form', clear_on_submit=True):
    submitted = st.form_submit_button('Submit')
    if submitted :
        with st.spinner('Calculating...'):
            response = generate_response(txt_input)
            result.append(response)

if len(result):
    st.info(response)
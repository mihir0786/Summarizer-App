# ======================
# IMPORTS AND SETUP
# ======================
import streamlit as st
from transformers import pipeline
import os
from dotenv import load_dotenv

# ======================
# CONFIGURATION
# ======================
# Load environment variables from .env file
load_dotenv()

# Set your Hugging Face API token
HF_API_TOKEN = os.environ["HF_API_TOKEN"] 

# ======================
# STREAMLIT UI SETUP
# ======================
# Page title
st.set_page_config(page_title='Summarization App', layout='wide')
st.title('📝 Summarization App')
st.markdown("""
    This app uses Facebook's BART-large-CNN model to generate concise summaries of your text.
    Paste your content below and click 'Submit' to get started.
""")

# ======================
# MODEL LOADING
# ======================
@st.cache_resource
def load_summarizer():
    """Load and cache the summarization pipeline to improve performance"""
    try:
        summarizer = pipeline(
            "summarization", 
            model="facebook/bart-large-cnn", 
            token=HF_API_TOKEN
        )
        return summarizer
    except Exception as e:
        st.error(f"Failed to load model: {str(e)}")
        return None

# ======================
# TEXT PROCESSING LOGIC
# ======================
def split_text_into_chunks(text, max_chunk=1024):
    """Split long text into manageable chunks for the model"""
    words = text.split()
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
    
    return chunks

def generate_summary_chunk(chunk, summarizer):
    """Generate summary for a single text chunk"""
    return summarizer(
        chunk,
        max_length=230,
        min_length=50,
        do_sample=False
    )[0]['summary_text']

def generate_response(txt):
    """Main function to handle text summarization"""
    if not txt.strip():
        return "Please enter some text to summarize."
    
    summarizer = load_summarizer()
    if summarizer is None:
        return "Model failed to load. Please check your API token and try again."
    
    # Handle long texts by splitting
    max_chunk_size = 1024
    if len(txt) > max_chunk_size:
        chunks = split_text_into_chunks(txt, max_chunk_size)
        summaries = []
        
        with st.status("Processing large text...", expanded=True) as status:
            progress_bar = st.progress(0)
            
            for i, chunk in enumerate(chunks):
                if len(chunk) > 100:  # Only summarize substantial chunks
                    summaries.append(generate_summary_chunk(chunk, summarizer))
                    progress_bar.progress((i+1)/len(chunks))
            
            status.update(label="Summary complete!", state="complete")
        
        return " ".join(summaries)
    else:
        # Direct summarization for shorter texts
        return generate_summary_chunk(txt, summarizer)

# ======================
# USER INTERFACE
# ======================
# Text input area
with st.container():
    st.subheader("Input Text")
    txt_input = st.text_area(
        'Enter your text to summarize', 
        '', 
        height=300,
        placeholder="Paste your article, report, or any long text here..."
    )

# Results display
result = []
with st.form('summarize_form'):
    submitted = st.form_submit_button('Generate Summary', type='primary')
    
    if submitted:
        with st.spinner('Analyzing text and generating summary...'):
            response = generate_response(txt_input)
            result.append(response)

if len(result):
    st.divider()
    st.subheader("Summary")
    st.success(response)
    st.info(f"Summary length: {len(response.split())} words (original: {len(txt_input.split())} words)")

# ==============================================
# IMPORTS AND INITIAL SETUP
# ==============================================
import streamlit as st
from transformers import pipeline
import os
from dotenv import load_dotenv
import logging
import hashlib
import time

# Configure logging to help with debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ==============================================
# CONFIGURATION AND ENVIRONMENT SETUP
# ==============================================
# Load environment variables safely
load_dotenv()

# Handle API token configuration
try:
    HF_API_TOKEN = os.environ["HF_API_TOKEN_2"]
except KeyError as e:
    st.error("🔑 HF_API_TOKEN not found in environment variables. Please check your .env file.")
    st.stop()

# ==============================================
# STREAMLIT UI CONFIGURATION
# ==============================================
# Configure page settings
st.set_page_config(
    page_title='📝 Summarization Model',
    layout="centered"
)

# Main title and description
st.title('📝 Text Summarization Application ')
st.markdown("""
    Transform lengthy documents into concise summaries using advanced NLP technology.
    Perfect for researchers, students, and professionals.
""")

# ==============================================
# USER PREFERENCES (SIDEBAR)
# ==============================================
with st.sidebar:
    st.header("⚙️ Customization Panel")
    
    # Summary length selection
    summary_length = st.selectbox(
        "Summary Density",
        ["Concise", "Balanced", "Detailed"],
        index=1,
        help="Control how condensed the summary should be"
    )
    
    # Length parameter mapping
    length_params = {
        "Concise": {"max_length": 80, "min_length": 40},
        "Balanced": {"max_length": 150, "min_length": 90},
        "Detailed": {"max_length": 300, "min_length": 200}
    }

# ==============================================
# TEXT INPUT SECTION
# ==============================================
# Enhanced text input area
txt_input = st.text_area(
    '📋 Paste your content here', 
    '', 
    height=300,
    placeholder="Paste your article, report, or any text you want summarized...",
    help="For best results, provide at least 2-3 paragraphs of text"
)

# Real-time text statistics
if txt_input:
    char_count = len(txt_input)
    word_count = len(txt_input.split())
    
    # Display metrics in columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📝 Characters", char_count)
    with col2:
        st.metric("🔠 Words", word_count)
    with col3:
        st.metric("⏱ Est. Time", f"{max(2, word_count // 100)} sec")
    
    # Input validation warning
    if char_count < 100:
        st.warning("ℹ️ Longer texts generally produce better summaries (100+ chars recommended)")

# ==============================================
# MODEL LOADING AND CACHING
# ==============================================
@st.cache_resource(show_spinner=False)
def load_summarizer():
    """Load and cache the summarization model with robust error handling"""
    try:
        logger.info("Loading FLAN-T5 summarization model...")
        return pipeline(
            "text2text-generation", 
            model="google/flan-t5-large", 
            token=HF_API_TOKEN,
            device="cpu"
        )
    except Exception as e:
        logger.error(f"Model loading failed: {str(e)}")
        st.error("🚨 Model initialization failed. Please check your API token.")
        return None

# ==============================================
# TEXT PROCESSING UTILITIES
# ==============================================
def smart_text_chunking(text, max_chunk_size=1024):
    """
    Advanced text segmentation that preserves:
    - Paragraph boundaries
    - Contextual continuity
    - Logical section breaks
    """
    if len(text) <= max_chunk_size:
        return [text]
    
    # First try splitting by paragraphs
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""
    
    for para in paragraphs:
        if len(current_chunk) + len(para) < max_chunk_size:
            current_chunk += para + "\n\n"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    # If still too large, fall back to sentence splitting
    if any(len(chunk) > max_chunk_size * 1.2 for chunk in chunks):
        return simple_word_chunking(text, max_chunk_size)
    
    return chunks

def simple_word_chunking(text, max_chunk_size):
    """Fallback chunking method for very long paragraphs"""
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) < max_chunk_size:
            current_chunk.append(word)
            current_length += len(word) + 1
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word)
    
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    return chunks

# ==============================================
# CORE SUMMARIZATION LOGIC
# ==============================================
@st.cache_data(ttl=3600, show_spinner=False)
def generate_response(txt, max_len, min_len):
    """
    Main summarization function with:
    - Intelligent chunk handling
    - Progress feedback
    - Comprehensive error handling
    """
    # Input validation
    if not txt or not txt.strip():
        return "❌ Please enter valid text to summarize"
    
    if len(txt.strip()) < 50:
        return "📏 Text too short (minimum 50 characters required)"
    
    try:
        summarizer = load_summarizer()
        if not summarizer:
            return "⚙️ Model unavailable - please try again later"
        
        # Generate appropriate prompt based on length
        base_prompt = """You are given a detailed passage. Write a well-structured and non-repetitive summary with the following sections:

                        1. **Key Points** – Highlight the core ideas or arguments.
                        2. **Important Details** – Include relevant supporting information or examples.
                        3. **Main Conclusions** – Summarize the overall insights or takeaways.
                    Ensure clarity, logical flow, and avoid repeating the original wording directly.

                    Text to summarize:{text}
                    """

        
        # Process based on text length
        if len(txt) > 1024:
            chunks = smart_text_chunking(txt)
            summaries = []
            progress_bar = st.progress(0)
            
            for i, chunk in enumerate(chunks):
                                
                try:
                    chunk_prompt = base_prompt.format(text=chunk)
                    output = summarizer(
                        chunk_prompt,
                        max_length=max(90, max_len // len(chunks)),
                        do_sample=False
                    )
                    summaries.append(output[0]['generated_text'])
                except Exception as e:
                    logger.warning(f"Chunk {i} failed: {str(e)}")
                    continue
                
                progress_bar.progress((i + 1) / len(chunks))
            
            progress_bar.empty()
            return "\n\n".join(summaries) if summaries else "Failed to generate summary"
        else:
            # Direct processing for shorter texts
            full_prompt = base_prompt.format(text=txt)
            output = summarizer(
                full_prompt,
                max_length=max_len,
                do_sample=False
            )
            return output[0]['generated_text']
            
    except Exception as e:
        logger.error(f"Summarization error: {str(e)}")
        return f"⚠️ Error during processing: {str(e)}"

# ==============================================
# MAIN APPLICATION FLOW
# ==============================================
# Form for submission
with st.form(key='summary_form'):
    submitted = st.form_submit_button(
        '🚀 Generate Summary', 
        use_container_width=True,
        help="Click to process your text"
    )
    
    if submitted:
        if not txt_input.strip():
            st.warning("📝 Please enter text before submitting")
        else:
            start_time = time.time()
            params = length_params[summary_length]
            
            with st.spinner(f'✨ Crafting {summary_length.lower()} summary...'):
                response = generate_response(
                    txt_input,
                    params["max_length"],
                    params["min_length"]
                )
                processing_time = time.time() - start_time
            
            # Display results
            st.success(f"✅ Summary ready! ({processing_time:.1f}s)")
            st.session_state.last_summary = response

# Display and export results
if 'last_summary' in st.session_state:
    st.divider()
    st.subheader("📄 Summary Output")
    
    # Summary display with expandable raw view
    with st.expander("View Formatted Summary", expanded=True):
        st.write(st.session_state.last_summary)
    
    # Export options
    export_col1, export_col2 = st.columns(2)
    with export_col1:
        st.download_button(
            label="💾 Save as TXT",
            data=st.session_state.last_summary,
            file_name="summary.txt",
            mime="text/plain"
        )
    

# Summarizer-App

Streamlit-based text summarization app using Hugging Face Transformers

- Implemented a web UI using Streamlit for text summarization.
- Integrated Hugging Face's `facebook/bart-large-cnn` model via `transformers.pipeline`.
- Added support for API token loading via `.env` file using `python-dotenv`.
- Automatically splits long input text into manageable chunks for summarization.
- Caches the summarizer model for performance efficiency.
- Displays summarized output in a user-friendly format.

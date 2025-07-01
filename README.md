📝 Summarizer App
A modern, AI-powered text summarization application built with Streamlit and Hugging Face Transformers. This application leverages the state-of-the-art BART model to provide accurate and concise summaries of long-form text content.
🌟 Features

Intelligent Text Summarization: Powered by Facebook's BART-large-CNN model from Hugging Face
Smart Text Chunking: Automatically handles long texts by splitting them into manageable chunks
Performance Optimized: Model caching for faster subsequent summarizations
User-Friendly Interface: Clean, intuitive Streamlit web interface
Secure API Management: Environment-based API token configuration
Real-time Processing: Interactive form with loading indicators

🚀 Demo
Show Image
🛠️ Technology Stack

Frontend: Streamlit
AI/ML: Hugging Face Transformers
Model: facebook/bart-large-cnn
Environment Management: python-dotenv
Language: Python 3.7+

📋 Prerequisites
Before running the application, ensure you have:

Python 3.7 or higher installed
A Hugging Face account and API token
Git (for cloning the repository)

⚡ Quick Start
1. Clone the Repository
bashgit clone https://github.com/yourusername/summarizer-app.git
cd summarizer-app
2. Install Dependencies
bashpip install -r requirements.txt
3. Environment Setup
Create a .env file in the root directory:
envHF_API_TOKEN=your_hugging_face_api_token_here
How to get your Hugging Face API Token:

Visit Hugging Face
Sign up/Login to your account
Go to Settings → Access Tokens
Create a new token with read permissions
Copy the token to your .env file

4. Run the Application
bashstreamlit run Summary2.py
The application will open in your default browser at http://localhost:8501

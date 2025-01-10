import streamlit as st
from streamlit_chat import message
import time
import random

# Configure the Streamlit page
st.set_page_config(page_title="StudySathi", page_icon="📚", layout="wide")

# Custom CSS to style the app with a dark theme
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        background-color: #0E1117;
        color: #E0E0E0;
    }

    /* Header styling */
    .stApp header {
        background-color: #0E1117;
        border-bottom: 1px solid #1E2127;
    }

    /* Sidebar styling */
    .css-1d391kg {
        background-color: #1E2127;
    }
            .mic-box {
        position: relative;
        width: 40px;
        height: 40px;
        background-color: #262730;
        border-radius: 1rem;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        margin-top: 100px;
    }

    .mic-box:hover {
        background-color: #363940;
    }

    .mic-icon {
        color: #E0E0E0;
        font-size: 1.2rem;
    }

    /* Input box styling */
    .stTextInput > div > div > input {
        background-color: #262730;
        border: 1px solid #363940;
        border-radius: 2rem;
        padding: 1rem;
        font-size: 1rem;
        color: #E0E0E0;
        width: 100%;
    }

    /* File uploader styling in sidebar */
    .sidebar .stFileUploader > div {
        background-color: #262730;
        border: 2px dashed #363940;
        border-radius: 1rem;
        padding: 1rem;
        font-size: 0.9rem;
        color: #E0E0E0;
        width: 100%;
        text-align: center;
        margin: 1rem 0;
    }

    /* Button styling */
    .stButton > button {
        background-color: #262730;
        border: 1px solid #363940;
        border-radius: 1rem;
        padding: 0.5rem 1rem;
        color: #E0E0E0;
        width: 100%;
    }

    .stButton > button:hover {
        background-color: #363940;
        border-color: #464B55;
        color: #FFFFFF;
    }

    /* Chat message styling */
    .message {
        padding: 1rem;
        border-radius: 1rem;
        margin-bottom: 0.5rem;
    }

    .user-message {
        background-color: #262730;
    }

    .bot-message {
        background-color: #1E2127;
        border: 1px solid #363940;
    }

    /* Title styling */
    h1 {
        text-align: center;
        color: #E0E0E0;
        font-size: 2.5rem !important;
        margin-bottom: 2rem !important;
    }

    /* Dark theme overrides */
    .stApp {
        background-color: #0E1117;
    }

    /* Input container with mic button */
    .input-container {
        position: relative;
        display: flex;
        align-items: center;
        margin-bottom: 1rem;
    }

    .mic-box {
        position: relative;
        display: flex;
        align-items: center;
        background-color: #262730;
        border-radius: 1rem;
        border: 2px solid #363940;
        padding: 0.5rem;
        color: #E0E0E0;
        cursor: pointer;
        width: fit-content;
        transition: background-color 0.3s, border-color 0.3s;
        margin-top: 25px;
    }

    .mic-box:hover {
        background-color: #363940;
        border-color: #464B55;
    }

    .mic-icon {
        color: #E0E0E0;
        font-size: 1.2rem;
    }

    .mic-text {
        font-size: 0.9rem;
        color: #FFFFFF;
    }

    /* Custom file upload text */
    .upload-text {
        color: #E0E0E0;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'last_input' not in st.session_state:
    st.session_state.last_input = ""
if 'is_recording' not in st.session_state:
    st.session_state.is_recording = False

# Sidebar
with st.sidebar:
    st.title("StudySathi")
    st.markdown("---")
    
    # New Chat button
    if st.button("+ New Chat", key="new_chat"):
        st.session_state.messages = []
        st.session_state.last_input = ""
    
    # File uploader in sidebar
    st.markdown('<p class="upload-text">Upload Files</p>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", 
                                   type=["txt", "pdf"], 
                                   label_visibility="collapsed")

# Main content
st.title("What can I help you learn?")

# Quick action buttons in two columns
col1, col2 = st.columns(2)
with col1:
    if st.button("📝 Generate Study Notes", key="notes"):
        st.session_state.messages.append({
            "content": "I'd like to generate study notes.",
            "is_user": True
        })

with col2:
    if st.button("🎯 Practice Problems", key="practice"):
        st.session_state.messages.append({
            "content": "I'd like to practice some problems.",
            "is_user": True
        })

# Chat history
for i, msg in enumerate(st.session_state.messages):
    message(msg['content'], is_user=msg['is_user'], key=f"msg_{i}")

# Chat input section with mic button
st.markdown('<div id="fixed-input">', unsafe_allow_html=True)
with st.form(key="chat_form"):
    col1, col2 = st.columns([1.2, 0.1])
    with col1:
        user_input = st.text_input("", 
                                 placeholder="Ask StudySathi a question...",
                                 key="user_input")
    with col2:
       with st.container():
            st.markdown(""" 
                <div class="mic-box" title="Voice Input">
                    <i class="fas fa-microphone mic-icon"></i>
                    <span class="mic-text">Voice</span>
                </div>
            """, unsafe_allow_html=True)
    
    submitted = st.form_submit_button("Submit")

st.markdown('</div>', unsafe_allow_html=True)

# Handle user input
if submitted and user_input:
    # Add user message to chat
    st.session_state.messages.append({"content": user_input, "is_user": True})
    st.session_state.last_input = user_input

    # Bot response
    with st.spinner("Thinking..."):
        try:
            response = f"I understand you're asking about {user_input}. Let me help you with that..."
            st.session_state.messages.append({"content": response, "is_user": False})
        except Exception as e:
            st.error(f"An error occurred: {str(e)}. Please try again.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #7A7F8C; font-size: 0.875rem;'>
        StudySathi - Your AI Study Companion
    </div>
    """,
    unsafe_allow_html=True
)

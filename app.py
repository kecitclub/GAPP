import streamlit as st
from datetime import datetime

st.set_page_config(page_title="StudyJedi", page_icon="🧠", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .stApp {
        background-color: #1E1E1E;
        color: #E0E0E0;
    }
    .stTextInput > div > div > input {
        background-color: #2D2D2D;
        color: #E0E0E0;
        border: 1px solid #4CAF50;
        padding: 0.5rem;
        border-radius: 10px;
        font-size: 1rem;
    }
    .stFileUploader > div {
        background-color: #2D2D2D;
        color: #E0E0E0;
        border: 1px solid #4CAF50;
        border-radius: 10px;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border: none;
        cursor: pointer;
        border-radius: 50%;
        padding: 0.5rem 1rem;
        font-size: 1.5rem;
    }
    .stButton > button:hover {
        background-color: #45A049;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        font-size: 1rem;
    }
    .chat-message.user {
        background-color: #2D2D2D;
    }
    .chat-message.bot {
        background-color: #3D3D3D;
    }
    .recommendation {
        background-color: #4A4A4A;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-top: 1rem;
        color: white;
    }
    footer {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Title
st.title("StudyJedi 🧠📚")

# Display chat history
st.header("Chat with StudyJedi")
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Fixed user input section at the bottom
with st.form(key="user_input_form"):
    col1, col2, col3 = st.columns([6, 2, 1])

    with col1:
        user_input = st.text_input(
            "Ask StudyJedi...",
            placeholder="Enter your question here...",
            label_visibility="collapsed",
        )
    with col2:
        uploaded_file = st.file_uploader("", label_visibility="collapsed", help="Upload files or images")
    with col3:
        submit = st.form_submit_button("↩", help="Send your query")

# Processing user input
if submit and user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    bot_response = f"Greetings, young Padawan! You asked: '{user_input}'. A Jedi's strength flows from knowledge. Let me share some wisdom with you."
    st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.write(bot_response)

        st.markdown("### 📚 Book Recommendation")
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(
                "https://m.media-amazon.com/images/I/51h9WbFPfxL.jpg",
                caption="The Jedi Path: A Manual for Students of the Force",
                use_container_width=True,
            )
        with col2:
            st.markdown("""
            **Title**: The Jedi Path: A Manual for Students of the Force  
            **Author**: Daniel Wallace  
            **Description**:  
            Discover the secrets of the Jedi Order with this ancient text passed down through generations. Learn the ways of the Force, Jedi philosophy, and training methods.
            """)

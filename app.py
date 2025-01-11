import streamlit as st
from streamlit_chat import message
from llama_cpp import Llama
import speech_recognition as sr
from Chunking import ChunkData
from Book import Book
from Video import Video

def load_model():
    if "llm" not in st.session_state:
        st.session_state.llm = Llama(model_path="unsloth.Q8_0 (1).gguf", n_ctx=2048)

def transcribe_audio(recognizer):
    with sr.Microphone() as source:
        st.info("Listening... Speak now!")
        try:
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source)
            # Listen to the microphone
            audio = recognizer.listen(source, timeout=15,phrase_time_limit=5)
            # Perform speech recognition
            text = recognizer.recognize_google(audio, language="ne-NP")
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand the audio."
        except sr.RequestError as e:
            return f"API error: {e}"
        except Exception as e:
            return f"Error: {str(e)}"


def main():
    
    load_model()
    
    book = Book()
    video = Video()

    chunks = ChunkData()

    recognizer = sr.Recognizer()

    if 'book_recommend' not in st.session_state:
        st.session_state.book_recommend = False
    # # Load the LLaMA model
    # llm = Llama(model_path="unsloth.Q8_0.gguf",n_ctx=2048)
    
    # Initialize the conversation history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    
    # Configure the Streamlit page
    st.set_page_config(page_title="StudySathi", page_icon="📚", layout="wide")

    # Sidebar
    with st.sidebar:
        st.title("Study Sathi")
        st.markdown("---")
        
        # New Chat button
        if st.button("+ New Chat", key="new_chat"):
            ## To Do
            # Create new chat 
            st.session_state.messages = []
            st.session_state.last_input = ""
        
        # File uploader in sidebar for OCR
        st.markdown('<p class="upload-text">Upload files for OCR</p>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("", 
                                    type=["txt", "pdf","jpg","png"], 
                                    label_visibility="collapsed")

    # Main content

    st.subheader("What can I help you learn?")

    # Capture input from the user
    st.session_state.user_input = st.chat_input(placeholder="Ask me a question...")

    # Quick action buttons in two columns
    col1,col3,ext2,ext3 = st.columns([2,2,1,2])
    with col1:
        book_input = st.text_input("Search Book",label_visibility="collapsed")
    with col1:
        if st.button("📝 Get Book Recommendations", key="books"):
            st.write(book_input)
            if book_input:
                titles,descriptions,images,book_links,authors = book.fetch_book_details(book_input)
                for title,description,image,book_link,author in zip(titles,descriptions,images,book_links,authors):
                    authors_str = ", ".join(author)
                    col1, col2 = st.columns([1, 5])
                    with col1:
                        # Using HTML to control the image size
                        st.markdown(f'<img src="{image}" alt="Book Cover" width="80">', unsafe_allow_html=True)
                    with col2:
                        st.write(f"**{title}**")
                        st.write(f"**Authors:** {authors_str}")
                        st.write(f"[More Info]({book_link})")
                        st.session_state.book_recommend = True

    with col3:
        video_input = st.text_input("Search Video",label_visibility="collapsed")

    with col3:
        if st.button("🎯 Get Video Recommendations", key="videos"):
            if video_input:
                titles,video_links,thumbnails = video.fetch_youtube_links(video_input,max_results=2)
                for title,video_link,thumbnail in zip(titles,video_links,thumbnails):
                    col1, col2 = st.columns([1, 5])
                    with col1:
                        # Using HTML to control the image size
                        st.markdown(f'<img src="{thumbnail}" alt="Book Cover" width="80">', unsafe_allow_html=True)
                    with col2:
                        st.write(f"**{title}**")
                        st.write(f"[Watch Here]({video_link})")

    with ext2:
        if st.button(label="🎙️"):
            st.session_state.user_input = transcribe_audio(recognizer)
            st.write(st.session_state.user_input)

    # if st.session_state.book_recommend:
        

    # st.markdown('<div style="height: 200px;"></div>', unsafe_allow_html=True)

    # Capture input from both chat input and microphone
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""

    # # Main input from the user
    # if st.session_state.user_input == "":
    #     st.session_state.user_input = st.chat_input(placeholder="Ask me a question...")

    # Display chat history
    for message in st.session_state.messages[-5:]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])




    # if user_input or st.session_state.user_input:
    #     if user_input:
    #         # Update user input from chat_input or microphone transcription
    #         st.session_state.user_input = user_input
    
    if st.session_state.user_input:
        # Add the user's message to the history
        st.session_state.messages.append({"role": "user", "content": st.session_state.user_input})
        
        # Display the user's message
        with st.chat_message("user"):
            st.markdown(st.session_state.user_input)

        history = st.session_state.messages[-5:]
        # Generate the response using a cleaner prompt structure
       
        conversation_history = "\n".join(
            [f"{msg['role'].capitalize()}: {msg['content']}" for msg in history]
        )

        full_prompt = f"{conversation_history}\nassistant (Respond in same language as in query):"

        # Generate the assistant's response
        response_text = ""
        with st.chat_message("assistant"):
            response_container = st.empty()
            for chunk in st.session_state.llm(full_prompt, stop=["User:", "Assistant:"], stream=True,max_tokens=200):
                response_text += chunk['choices'][0]['text']
                response_container.markdown(response_text)

        # Add the assistant's message to the history
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        # Clear user input after response
        st.session_state.user_input = ""
        user_input=""



if __name__ == "__main__":
    main()
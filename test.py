from Book import Book
from youtubeApi import fetch_youtube_links
from Variable import Variable
import streamlit as st

# book = Book()
# titles,descriptions,images,book_links,authors = book.fetch_book_details("Computer Networks")

# for title,author,image,book_link,description in zip(titles,authors,images,book_links,descriptions):
#     authors_str = ", ".join(author)
#     print(f"Title: {title}\nAuthors: {authors_str}\nDescription: {description}\nCover Image: {image}\nMore Info: {book_link}\n")


# links = fetch_youtube_links(Variable.get_variable("youtube_api_key"), "Computer Networks",max_results=5)
# for link in links:
#     print(link)

def main():

    # Initiate LLM
    model = ""
    # Initiate Book Classfrom Video import Video

    book = Book()
    # Initiate Video Class
    video = ""

    # Take input: Question or Syllabus (Handle ocr also later on)
    question = ""
    syllabus = ""
    ocr = ""
    audio = ""

    if question or audio:
        # Handle if the input is question in text or audio form
        if audio:
            # Process audio to text
            pass
        # Hold conversation with user
        pass

    if syllabus or ocr:
        # Handle if the input is text-syllabus or ocr-syllabus
        if ocr:
            # Extract text from image
            # Format the text
            pass
        # Chunk the text
        chunks=[]
        # Feed the chunks to LLM 
        for chunk in chunks:
            # Generate keywords from each chunk
            keywords = []
            for keyword in keywords:
                # Send the keywords to google books api and youtube video api
                results_book = book.fetch_book_details(keyword)
                # Send output to streamlit app 
                results_video = ""
                # Send output to streamlit app
        pass

    


    st.title("Study Sathi")
    search_query = st.text_input(label="Enter a text",label_visibility="hidden")

if __name__ == "__main__":
    main()

video = Video()
SEARCH_TERM = "Python programming"

video_links = video.fetch_youtube_links(SEARCH_TERM)

# Print the fetched links
for i, video_links in enumerate(video_links, 1):
    print(f"{i}. {video_links}")
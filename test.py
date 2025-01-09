from Book import Book
from Video import Video
from Variable import Variable
import streamlit as st

# # book = Book()
# # titles,descriptions,images,book_links,authors = book.fetch_book_details("Computer Networks")

# for title,author,image,book_link,description in zip(titles,authors,images,book_links,descriptions):
#     authors_str = ", ".join(author)
#     print(f"Title: {title}\nAuthors: {authors_str}\nDescription: {description}\nCover Image: {image}\nMore Info: {book_link}\n")


# # links = fetch_youtube_links(Variable.get_variable("youtube_api_key"), "Computer Networks",max_results=5)
# # for link in links:
# #     print(link)

def main():

    # Initiate LLM
    model = ""
    # Initiate Book Class
    book = Book()
    # Initiate Video Class
    video = Video()

    st.title("Study Sathi")
    search_query = st.text_input(label="Enter a text",label_visibility="hidden")

    # Take input: Question or Syllabus (Handle ocr also later on)
    question = ""
    syllabus = 1
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
        chunks=[1]
        for chunk in chunks:
            # Feed the chunks to LLM 

            # Generate keywords from each chunk
            keywords = ["TCP/IP","OSI Model"]
            col_l,col_r = st.columns([1,1])
            with col_l:
                st.markdown("### 📚 Book Recommendation\n")
                for keyword in keywords:
                    # Send the keywords to google books api
                    titles,descriptions,images,book_links,authors = book.fetch_book_details(keyword)

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
                
            # Send output to streamlit app 
            with col_r:
                st.markdown("### Video Recommendation\n")
                for keyword in keywords:
                    # Send the keywords to youtube video api
                    titles,video_links,thumbnails = video.fetch_youtube_links(keyword,max_results=2)

                    for title,video_link,thumbnail in zip(titles,video_links,thumbnails):
                        col1, col2 = st.columns([1, 5])
                        with col1:
                            # Using HTML to control the image size
                            st.markdown(f'<img src="{thumbnail}" alt="Book Cover" width="80">', unsafe_allow_html=True)
                        with col2:
                            st.write(f"**{title}**")
                            st.write(f"[Watch Here]({video_link})")
                    
                # results_video = video.fetch_youtube_links()
                # Send output to streamlit app
        pass

    


    

if __name__ == "__main__":
    main()


# from Video import Video

# video = Video()

# titles,video_links,thumbnails = video.fetch_youtube_links("Computer Network")

# for title,video_link,thumbnail in zip(titles,video_links,thumbnails):
#     print(f"Title: {title}\nThumbnail: {thumbnail}\nLink: {video_link}\n")
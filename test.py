from Book import Book
from Video import Video

book = Book()
titles,descriptions,images,book_links,authors = book.fetch_book_details("Computer Networks")

for title,author,image,book_link,description in zip(titles,authors,images,book_links,descriptions):
    authors_str = ", ".join(author)
    print(f"Title: {title}\nAuthors: {authors_str}\nDescription: {description}\nCover Image: {image}\nMore Info: {book_link}\n")

video = Video()
SEARCH_TERM = "Python programming"

video_links = video.fetch_youtube_links(SEARCH_TERM)

# Print the fetched links
for i, video_links in enumerate(video_links, 1):
    print(f"{i}. {video_links}")
from Book import Book

book = Book()
titles,descriptions,images,book_links,authors = book.fetch_book_details("Computer Networks")

for title,author,image,book_link,description in zip(titles,authors,images,book_links,descriptions):
    authors_str = ", ".join(author)
    print(f"Title: {title}\nAuthors: {authors_str}\nDescription: {description}\nCover Image: {image}\nMore Info: {book_link}\n")
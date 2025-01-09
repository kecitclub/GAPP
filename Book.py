from Variable import Variable
import requests

class Book:
    def __init__(self):
        self.api_key = Variable.get_variable("books_api_key")

    def fetch_book_details(self,query):

        url = f"https://www.googleapis.com/books/v1/volumes?q={query}&printType=books&key={self.api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            titles = []
            authors = []
            images = []
            book_links = []
            descriptions = []

            books = response.json().get('items', [])
            for book in books[:2]:  # Displaying top 5 results
                volume_info = book.get('volumeInfo', {})
                title = volume_info.get('title', 'N/A')
                description = volume_info.get('description', 'Description not available.')
                author = volume_info.get('authors', 'N/A')
                link = volume_info.get('infoLink', '#')
                # Fetching book cover image
                image_link = volume_info.get('imageLinks', {}).get('smallThumbnail', 'No Image Available')

                titles.append(title)
                descriptions.append(description)
                images.append(image_link)
                book_links.append(link)
                authors.append(author)

            return titles,descriptions,images,book_links,authors

        


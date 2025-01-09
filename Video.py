from Variable import Variable
import requests

class Video:
    def __init__(self):
        self.api_key = Variable.get_variable("youtube_api_key")
    
    def fetch_youtube_links(self, search_term, max_results=5):
        # YouTube Data API base URL
        url = "https://www.googleapis.com/youtube/v3/search"
        
        # Query parameters
        params = {
            "part": "snippet",  # We need the snippet for video titles
            "q": search_term,   # Search term
            "type": "video",    # We are looking for videos
            "maxResults": max_results,  # Number of results to fetch
            "key": self.api_key,
            "order": "relevance"   
        }
        
        # Make the GET request
        response = requests.get(url, params=params)
        # Order by views????
        if response.status_code == 200:
            # Parse the response JSON
            data = response.json()
            video_links = []
            titles = []
            thumbnails = []
            # Extract video links from the response
            for item in data.get("items", []):
                title = item["snippet"]["title"]
                thumbnail = item["snippet"]["thumbnails"]["default"]["url"]
                video_id = item["id"]["videoId"]
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                video_links.append(video_url)
                titles.append(title)
                thumbnails.append(thumbnail)
            
            return titles,video_links,thumbnails
        else:
            # Print the error message if the request fails
            print(f"Error: {response.status_code}")
            print(response.json())
            return []

    


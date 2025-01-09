import requests

def fetch_youtube_links(api_key, search_term, max_results=10):
    # YouTube Data API base URL
    url = "https://www.googleapis.com/youtube/v3/search"
    
    # Query parameters
    params = {
        "part": "snippet",  # We need the snippet for video titles
        "q": search_term,   # Search term
        "type": "video",    # We are looking for videos
        "maxResults": max_results,  # Number of results to fetch
        "key": api_key      # Your API key
    }
    
    # Make the GET request
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()
        video_links = []
        
        # Extract video links from the response
        for item in data.get("items", []):
            video_id = item["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            video_links.append(video_url)
        
        return video_links
    else:
        # Print the error message if the request fails
        print(f"Error: {response.status_code}")
        print(response.json())
        return []

# Replace 'YOUR_API_KEY' with your actual YouTube Data API key
API_KEY = "AIzaSyCxcjIrR_-QXKIaHXLANConjWVnOpPNEp4"
SEARCH_TERM = "Python programming"

# Fetch video links
ytlinks = fetch_youtube_links(API_KEY, SEARCH_TERM)

# Print the fetched links
for i, ytlinks in enumerate(ytlinks, 1):
    print(f"{i}. {ytlinks}")

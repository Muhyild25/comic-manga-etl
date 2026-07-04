import requests

def get_top_manga():
    url = "https://api.jikan.moe/v4/top/manga"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['data'][:5] 
    else:
        print(f"Jikan API Hatasi: {response.status_code}")
        return []
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_top_comics():
    api_key = os.getenv("COMICVINE_API_KEY")
    if not api_key:
        print("Hata: COMICVINE_API_KEY bulunamadi!")
        return []
        
    url = f"https://comicvine.gamespot.com/api/volumes/?api_key={api_key}&format=json&limit=5"
    headers = {"User-Agent": "ComicMangaETL/1.0"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('results', []) 
    else:
        print(f"Comic Vine API Hatasi: {response.status_code}")
        return []
import requests
import os
from dotenv import load_dotenv

# .env dosyasindaki degiskenleri sisteme yukle
load_dotenv()

def get_top_comics():
    # API anahtarini artik guvenli bir sekilde .env dosyasindan cekiyoruz
    api_key = os.getenv("COMICVINE_API_KEY")
    
    if not api_key:
        print("Hata: COMICVINE_API_KEY bulunamadi! .env dosyanizi kontrol edin.")
        return
        
    url = f"https://comicvine.gamespot.com/api/volumes/?api_key={api_key}&format=json&limit=5"
    
    headers = {
        "User-Agent": "ComicMangaETL/1.0"
    }
    
    print("Comic Vine API'ye istek atiliyor...\n")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        
        print("--- POPULER BATI CIZGI ROMANLARI ---")
        for i, comic in enumerate(results):
            name = comic.get('name', 'Isimsiz')
            publisher_info = comic.get('publisher')
            publisher = publisher_info.get('name', 'Bilinmiyor') if publisher_info else 'Bilinmiyor'
            issues_count = comic.get('count_of_issues', 'Bilinmiyor')
            
            print(f"{i+1}. {name} | Yayinci: {publisher} | Sayi Adedi: {issues_count}")
    else:
        print(f"Hata! Durum Kodu: {response.status_code}")

if __name__ == "__main__":
    get_top_comics()

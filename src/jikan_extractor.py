import requests

def get_top_manga():
    # Jikan API uc noktasi
    url = "https://api.jikan.moe/v4/top/manga"
    print("Jikan API'ye istek atiliyor...\n")
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("--- EN POPULER 5 MANGA/MANHWA ---")
        for i, manga in enumerate(data['data'][:5]):
            title = manga.get('title', 'Isimsiz')
            score = manga.get('score', 'Puan Yok')
            manga_type = manga.get('type', 'Bilinmiyor')
            print(f"{i+1}. {title} | Tur: {manga_type} | Puan: {score}")
    else:
        print(f"Hata! Durum Kodu: {response.status_code}")

if __name__ == "__main__":
    get_top_manga()
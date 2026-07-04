import pandas as pd
from jikan_extractor import get_top_manga
from comicvine_extractor import get_top_comics

def transform_data():
    raw_manga = get_top_manga()
    raw_comics = get_top_comics()

    # Manga verilerini duzenleme
    manga_list = [{
        "Eser_Adi": item.get("title", "Isimsiz"),
        "Orijin": "Dogu (Manga)",
        "Tur_Yayinci": item.get("type", "Bilinmiyor"),
        "Skor_Sayi": item.get("score", 0)
    } for item in raw_manga]
    df_manga = pd.DataFrame(manga_list)

    # Comic verilerini duzenleme
    comic_list = []
    for item in raw_comics:
        publisher_info = item.get("publisher")
        publisher = publisher_info.get("name", "Bilinmiyor") if publisher_info else "Bilinmiyor"
        
        comic_list.append({
            "Eser_Adi": item.get("name", "Isimsiz"),
            "Orijin": "Bati (Comic)",
            "Tur_Yayinci": publisher,
            "Skor_Sayi": item.get("count_of_issues", 0)
        })
    df_comics = pd.DataFrame(comic_list)

    # Verisetlerini birlestirme
    df_final = pd.concat([df_manga, df_comics], ignore_index=True)
    return df_final

if __name__ == "__main__":
    df = transform_data()
    print(df.to_string())
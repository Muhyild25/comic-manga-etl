# Comic & Manga ETL Pipeline

Bu proje, Jikan API (Manga) ve Comic Vine API (Batý Çizgi Romanlarý) kullanarak farklý yapýdaki verileri çeken, Pandas ile temizleyip ortak bir formata dönüþtüren ve SQLite veritabanýna kaydeden temel bir ETL projesidir. 

Farklý kaynaklardan gelen JSON yapýlarýný tek bir þemada birleþtirme pratiði yapmak amacýyla geliþtirilmiþtir.

## Proje Adýmlarý

1. **Extract:** Jikan API ve Comic Vine API'ye istek atýlarak popüler seriler çekilir.
2. **Transform:** Gelen farklý JSON verileri Pandas kullanýlarak `[Eser_Adi, Orijin, Tur_Yayinci, Skor_Sayi]` ortak þemasýna dönüþtürülür.
3. **Load:** Temizlenen veriler lokal `comics_manga.db` SQLite veritabanýna kaydedilir.

## Kurulum ve Çalýþtýrma

Projeyi lokalinizde çalýþtýrmak için aþaðýdaki adýmlarý izleyebilirsiniz.

1. Depoyu klonlayýn ve klasöre gidin:
    git clone https://github.com/Muhyild25/comic-manga-etl.git
    cd comic-manga-etl

2. Gerekli kütüphaneleri kurun:
    pip install requests pandas python-dotenv

3. Ana dizinde bir .env dosyasý oluþturup Comic Vine API anahtarýnýzý ekleyin:
    COMICVINE_API_KEY=api_anahtariniz

4. Pipeline'ý baþlatýn:
    python src/loader.py

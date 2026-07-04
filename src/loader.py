import sqlite3
import os
from transformer import transform_data

def load_data():
    df_final = transform_data()
    db_path = os.path.join("data", "comics_manga.db")
    
    conn = sqlite3.connect(db_path)
    
    try:
        df_final.to_sql("popular_series", conn, if_exists="replace", index=False)
        print(f"ETL basarili: Veriler {db_path} konumuna kaydedildi.")
    except Exception as e:
        print(f"Veritabani hatasi: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    load_data()
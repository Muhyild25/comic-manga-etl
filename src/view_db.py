import sqlite3
import pandas as pd


conn = sqlite3.connect("data/comics_manga.db")


df = pd.read_sql_query("SELECT * FROM popular_series", conn)

print("\n=== VERITABANINDAKI GUNCEL VERILER ===")
print(df.to_string())

conn.close()
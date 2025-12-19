import sqlite3
import pandas as pd
from datetime import datetime
import random 

# --- CONFIGURATION ---
CRYPTOS = ['bitcoin', 'ethereum', 'solana', 'binance-coin']
DB_NAME = "crypto_database.db"

def get_mock_data():
    """Génération des données simulées"""
    print("Simulation des donnees...")
    fake_data = []
    base_prices = {'bitcoin': 95000, 'ethereum': 3500, 'solana': 140, 'binance-coin': 600}
    
    for crypto in CRYPTOS:
        variation = random.uniform(0.95, 1.05)
        price = base_prices.get(crypto, 100) * variation
        
        fake_data.append({
            'nom': crypto.capitalize(),
            'symbole': crypto[:3].upper(),
            'prix_usd': round(price, 2),
            'market_cap': round(price * 1000000, 2),
            'date_extraction': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return fake_data

def save_to_sqlite(data):
    """Sauvegarde les données dans une base SQL"""
    # 1. Connexion à la base (elle se crée toute seule si elle n'existe pas)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # 2. Création de la table (si elle n'existe pas déjà)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            symbole TEXT,
            prix_usd REAL,
            market_cap REAL,
            date_extraction TEXT
        )
    """)
    
    # 3. Insertion des données
    print("Sauvegarde en base de donnees SQL...")
    for item in data:
        cursor.execute("""
            INSERT INTO crypto_prices (nom, symbole, prix_usd, market_cap, date_extraction)
            VALUES (?, ?, ?, ?, ?)
        """, (item['nom'], item['symbole'], item['prix_usd'], item['market_cap'], item['date_extraction']))
    
    # 4. Validation et fermeture
    conn.commit()
    conn.close()
    print("Donnees inserees avec succes dans SQLite.")

def main():
    print("--- Pipeline ETL SQL ---")
    
    # Etape 1 : Extract / Transform
    data = get_mock_data()
    
    # Etape 2 : Load (SQL)
    if data:
        save_to_sqlite(data)
        
        # Verification : On relit la base pour prouver que cela a fonctionne
        conn = sqlite3.connect(DB_NAME)
        df_verif = pd.read_sql("SELECT * FROM crypto_prices ORDER BY id DESC LIMIT 10", conn)
        print("\nVerification (Dernieres lignes en base) :")
        print(df_verif)
        conn.close()

if __name__ == "__main__":
    main()
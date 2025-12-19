import pandas as pd
from datetime import datetime
import random
import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv # Import du chargeur de secrets

# --- CONFIGURATION ---
# 1. On charge les secrets du fichier .env
load_dotenv()

CRYPTOS = ['bitcoin', 'ethereum', 'solana', 'binance-coin']
FILENAME = "crypto_data.csv"
CONTAINER_NAME = "raw-data"

# 2. On recupere la cle de maniere securisee
# Si la cle n'est pas trouvee, le script s'arretera proprement
AZURE_CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")

def get_mock_data():
    """Generation des donnees simulees"""
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

def upload_to_azure(local_file_name):
    """Envoie le fichier CSV vers Azure Data Lake"""
    
    if not AZURE_CONNECTION_STRING:
        print("ERREUR : La variable d'environnement AZURE_CONNECTION_STRING est vide.")
        return

    print("Connexion a Azure...")
    
    try:
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=local_file_name)
        
        print(f"Envoi du fichier {local_file_name} vers le conteneur '{CONTAINER_NAME}'...")
        with open(local_file_name, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
            
        print("Succes ! Fichier transfere sur le Cloud Azure.")
        
    except Exception as e:
        print(f"Erreur Azure : {e}")

def main():
    print("--- Pipeline ETL Cloud (Securise) ---")
    
    # 1. Création local
    data = get_mock_data()
    df = pd.DataFrame(data)
    df.to_csv(FILENAME, index=False)
    print(f"Fichier local {FILENAME} genere.")
    
    # 2. Envoi Cloud
    upload_to_azure(FILENAME)

if __name__ == "__main__":
    main()
import pandas as pd
from datetime import datetime
import random 

# --- CONFIGURATION ---
# On simule ces cryptos
CRYPTOS = ['bitcoin', 'ethereum', 'solana', 'binance-coin']

def get_mock_data():
    """
    SIMULATION : Génère de fausses données réalistes.
    Permet de coder le pipeline même si le réseau bloque l'API réelle.
    """
    print(f"📡 Simulation de l'appel API (Mode hors-ligne)...")
    
    fake_data = []
    
    # Prix de base approximatifs
    base_prices = {
        'bitcoin': 95000, 
        'ethereum': 3500, 
        'solana': 140, 
        'binance-coin': 600
    }
    
    for crypto in CRYPTOS:
        # Variation aléatoire entre -5% et +5%
        variation = random.uniform(0.95, 1.05)
        price = base_prices.get(crypto, 100) * variation
        
        fake_data.append({
            'nom': crypto.capitalize(),
            'symbole': crypto[:3].upper(),
            'prix_usd': round(price, 2),
            'market_cap': round(price * 1000000, 2),
            'date_extraction': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': 'SIMULATION'
        })
        
    return fake_data

def main():
    print("--- Démarrage du Pipeline ETL ---")
    
    # 1. EXTRACTION
    data = get_mock_data()
    
    if data:
        # 2. CHARGEMENT
        df = pd.DataFrame(data)
        print("\n📊 Aperçu des données :")
        print(df)
        
        filename = "crypto_data.csv"
        df.to_csv(filename, index=False)
        print(f"\n✅ Succès ! Fichier '{filename}' généré.")
    else:
        print("⚠️ Erreur.")

if __name__ == "__main__":
    main()
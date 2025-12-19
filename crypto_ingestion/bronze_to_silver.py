import pandas as pd
import os

# --- CONFIGURATION DES CHEMINS ---
base_path = "data"
input_csv = os.path.join(base_path, "bronze", "crypto_data.csv")
output_parquet = os.path.join(base_path, "silver", "crypto_data.parquet")

# --- 1. LECTURE (BRONZE) ---
print(f"Lecture du fichier Bronze : {input_csv}")
if not os.path.exists(input_csv):
    print(f"❌ ERREUR CRITIQUE : Le fichier {input_csv} n'existe pas.")
    exit()

df = pd.read_csv(input_csv)

# --- 2. TRANSFORMATION (Vers SILVER) ---
print("Transformation et standardisation des données...")

# A. Typage des Dates (Avec le BON nom de colonne)
# Si cette ligne plante, c'est que tu n'as pas sauvegardé le fichier !
df['date_extraction'] = pd.to_datetime(df['date_extraction'], errors='coerce')

# B. Nettoyage et Typage des Nombres
cols_numeriques = ['prix_usd', 'market_cap']
for col in cols_numeriques:
    if col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.replace(',', '.', regex=False)
        df[col] = pd.to_numeric(df[col], errors='coerce')

# C. Renommage (Standardisation Schema Silver)
mapping_colonnes = {
    'nom': 'name',
    'symbole': 'symbol',
    'prix_usd': 'price_usd',
    'market_cap': 'market_cap', 
    'date_extraction': 'extraction_date'
}
df = df.rename(columns=mapping_colonnes)

# --- 3. ECRITURE (SILVER - PARQUET) ---
print(f"Sauvegarde du fichier Silver : {output_parquet}")

# Création du dossier parent si inexistant
os.makedirs(os.path.dirname(output_parquet), exist_ok=True)

# Ecriture en Parquet
df.to_parquet(output_parquet, engine='pyarrow', compression='snappy', index=False)

print("✅ SUCCÈS : Transformation Bronze -> Silver terminée.")
print("Aperçu du fichier Silver :")
print(df.head())
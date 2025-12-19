import pandas as pd
import os

# --- CONFIGURATION DES CHEMINS ---
base_path = "data"
input_silver = os.path.join(base_path, "silver", "crypto_data.parquet")
output_gold = os.path.join(base_path, "gold", "global_kpis.parquet")

# --- 1. LECTURE (SILVER) ---
print(f"Lecture des données Silver : {input_silver}")
if not os.path.exists(input_silver):
    print("❌ Erreur : Le fichier Silver n'existe pas. Lance bronze_to_silver.py d'abord !")
    exit()

df = pd.read_parquet(input_silver)

# --- 2. TRANSFORMATION (AGRÉGATION / GOLD) ---
print("Calcul des KPIs (Moyennes et Totaux)...")

# Équivalent SQL : SELECT AVG(price_usd) ...
avg_price = df['price_usd'].mean()

# Équivalent SQL : SELECT SUM(market_cap) ...
total_cap = df['market_cap'].sum()

# Création du DataFrame Gold (La table finale pour le rapport)
# On ajoute une colonne 'date_calcul' pour savoir quand le KPI a été généré
kpi_df = pd.DataFrame({
    'avg_price_usd': [avg_price],
    'total_market_cap': [total_cap],
    'calculation_date': [pd.Timestamp.now()]
})

# --- 3. ÉCRITURE (GOLD - PARQUET) ---
print(f"Sauvegarde des KPIs Gold : {output_gold}")

# Création du dossier gold
os.makedirs(os.path.dirname(output_gold), exist_ok=True)

# Sauvegarde
kpi_df.to_parquet(output_gold, engine='pyarrow', compression='snappy', index=False)

print("✅ SUCCÈS : KPIs générés dans la couche Gold !")
print("Aperçu de la table Gold :")
print(kpi_df)
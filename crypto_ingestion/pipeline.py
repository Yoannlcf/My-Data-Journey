import os
import time

# --- CONFIGURATION ---
# Liste des scripts à exécuter dans l'ordre
# 1. (Optionnel) main.py si tu veux régénérer la donnée à chaque fois
# 2. Upload vers Azure (Ingestion Cloud)
# 3. Transformations locales (Pour l'instant)
steps = [
    "upload_to_azure.py",    # ☁️ Ingestion vers le Cloud
    "bronze_to_silver.py",   # 🧹 Nettoyage (Local)
    "silver_to_gold.py"      # 📊 Agrégation (Local)
]

def run_step(script_name):
    print(f"🚀 Démarrage de : {script_name}...")
    start_time = time.time()
    
    # Exécution de la commande
    exit_code = os.system(f"python {script_name}")
    
    end_time = time.time()
    duration = round(end_time - start_time, 2)
    
    if exit_code == 0:
        print(f"✅ {script_name} terminé avec succès en {duration} secondes.\n")
        return True
    else:
        print(f"❌ ERREUR CRITIQUE sur {script_name}. Arrêt du pipeline.")
        return False

# --- DÉBUT DU PIPELINE ---
print("==============================================")
print("🤖 PIPELINE HYBRIDE (LOCAL + AZURE)")
print("==============================================\n")

all_success = True
for script in steps:
    if not run_step(script):
        all_success = False
        break

print("==============================================")
if all_success:
    print("🏁 FIN DU PIPELINE : Succès complet !")
else:
    print("💀 FIN DU PIPELINE : Échec.")
print("==============================================")
import os
import time

# Mon "Azure Data Factory" local
# Il orchestre l'exécution des scripts dans le bon ordre

def run_step(script_name):
    print(f"Démarrage de : {script_name}...")
    start_time = time.time()
    
    # os.system exécute une commande terminal comme si tu le faisais toi-même
    exit_code = os.system(f"python {script_name}")
    
    end_time = time.time()
    duration = round(end_time - start_time, 2)
    
    if exit_code == 0:
        print(f" {script_name} terminé avec succès en {duration} secondes.\n")
        return True
    else:
        print(f" ERREUR CRITIQUE sur {script_name}. Arrêt du pipeline.")
        return False

# --- DÉBUT DU PIPELINE ---
print("==============================================")
print(" DÉMARRAGE DU PIPELINE ETL CRYPTO")
print("==============================================\n")

# Étape 1 : Bronze -> Silver
if run_step("bronze_to_silver.py"):
    
    # Étape 2 : Silver -> Gold (ne se lance que si l'étape 1 a réussi)
    run_step("silver_to_gold.py")

print("==============================================")
print(" FIN DU PIPELINE")
print("==============================================")
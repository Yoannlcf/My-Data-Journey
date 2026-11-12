import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# 1. Chargement de la configuration (Sécurité)
load_dotenv()

connection_string = os.getenv("AZURE_CONNECTION_STRING")
if not connection_string:
    print("❌ ERREUR : La variable AZURE_CONNECTION_STRING est vide ou introuvable.")
    exit()

# 2. Configuration des chemins
# Le fichier local à envoyer
local_file_path = os.path.join("data", "bronze", "crypto_data.csv")
# Le nom du fichier tel qu'il apparaîtra sur Azure
blob_name = "crypto_data.csv"
# Le conteneur cible (que tu as créé)
container_name = "bronze"

def upload_file_to_azure():
    print(f"Tentative de connexion à Azure...")
    
    try:
        # A. Création du client de service 
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # B. Création du client de blob 
        # Note : On combine le conteneur et le nom du fichier
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        
        print(f"Envoi du fichier : {local_file_path} vers le conteneur '{container_name}'...")
        
        # C. Lecture et Upload du fichier
        # 'rb' = Read Binary (indispensable pour les fichiers, images, etc.)
        # overwrite=True : Écrase le fichier s'il existe déjà (comportement d'un ETL régulier)
        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
            
        print(f"SUCCÈS : Le fichier a été uploadé sur Azure !")
        print(f"Vérifie ici : https://portal.azure.com (Storage Browser > Bronze)")
        
    except FileNotFoundError:
        print(f"ERREUR : Le fichier local {local_file_path} n'existe pas.")
    except Exception as e:
        print(f"ERREUR AZURE : Une erreur s'est produite lors de l'envoi.")
        print(f"Détails : {e}")

if __name__ == "__main__":
    upload_file_to_azure()
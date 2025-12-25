import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()
connection_string = os.getenv("AZURE_CONNECTION_STRING")

print("🔍 Analyse de ton compte Azure...")

try:
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    # On liste tous les conteneurs existants
    containers = blob_service_client.list_containers()
    
    print("\n📦 Voici la liste des conteneurs trouvés :")
    found = False
    for container in containers:
        print(f" - {container.name}")
        found = True
        
    if not found:
        print("⚠️ Aucun conteneur trouvé ! Ton compte est vide.")
        print("👉 Retourne sur le portail Azure et crée le conteneur 'bronze'.")
    else:
        print("\nCompare ces noms avec 'bronze' (celui cherché par ton script).")

except Exception as e:
    print(f"❌ Erreur de connexion : {e}")
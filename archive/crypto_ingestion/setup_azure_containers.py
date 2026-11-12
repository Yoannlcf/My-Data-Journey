import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()
connection_string = os.getenv("AZURE_CONNECTION_STRING")

def fix_architecture():
    print("🔧 Réparation de l'architecture Cloud...")
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    # Nous voulons ces conteneurs à la racine
    targets = ["bronze", "silver", "gold", "scripts"]
    
    for name in targets:
        try:
            blob_service_client.create_container(name)
            print(f"✅ Conteneur '{name}' créé avec succès !")
        except Exception as e:
            if "ContainerAlreadyExists" in str(e):
                print(f"ℹ️  Le conteneur '{name}' existe déjà (Parfait).")
            else:
                print(f"❌ Erreur sur '{name}': {e}")

if __name__ == "__main__":
    fix_architecture()
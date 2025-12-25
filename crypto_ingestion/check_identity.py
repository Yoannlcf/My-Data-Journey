import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()
connection_string = os.getenv("AZURE_CONNECTION_STRING")

try:
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    # On récupère le nom du compte lié à la clé
    account_name = blob_service_client.account_name
    
    print("------------------------------------------------")
    print(f"🆔 Ton code est connecté au compte : {account_name}")
    print("------------------------------------------------")
    print("👉 Regarde maintenant sur le Portail Azure (en haut à gauche).")
    print(f"   Est-ce que le nom affiché est BIEN '{account_name}' ?")

except Exception as e:
    print(f"❌ Erreur : {e}")
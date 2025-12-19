# My-Data-Journey 🚀

Bienvenue sur mon portfolio technique ! 👋

Diplômé en Informatique (BUT & Bachelor UQAC), je consacre actuellement une année de césure à ma spécialisation intensive en **Data Engineering** et **Cloud Computing**.

Ce dépôt centralise mes projets d'apprentissage, mes POCs (Proof of Concepts) et mes pipelines de données, documentant ma progression vers les certifications **Azure** et **Databricks**.

## 🎯 Objectifs & Stack Technique

Mon focus se porte sur la "Modern Data Stack" et l'écosystème Cloud :

| Domaine | Technologies & Outils |
| :--- | :--- |
| **Langages** | 🐍 Python, 🗃️ SQL |
| **Cloud** | ☁️ Microsoft Azure (Data Lake Gen2, Storage Account) |
| **Processing** | ⚡ Apache Spark, 🧱 Databricks (À venir) |
| **Sécurité** | 🔐 Gestion des secrets (.env), IAM |
| **Qualité & CI/CD** | 🏗️ Git, GitHub Actions |

## 📂 Projets Réalisés

### 1. Crypto Ingestion Pipeline (ETL Hybride)
*Pipeline d'ingestion de données financières simulées vers le Cloud Azure.*

Ce projet démontre la mise en place d'une architecture ETL sécurisée connectant un script Python local à un Data Lake d'entreprise.

- **Architecture :** Python (Local) ➔ Transformation (Pandas) ➔ Azure Data Lake Gen2.
- **Compétences clés :**
    - **Extract :** Simulation de données API (Mocking) pour pallier les restrictions réseau.
    - **Load :** Connexion au SDK Azure Blob Storage.
    - **Sécurité :** Gestion des clés d'accès via variables d'environnement (`python-dotenv`) pour ne jamais exposer de secrets sur GitHub.
- **Stack :** Python, Pandas, Azure Storage Blob, SQLite.
- **Statut :** ✅ V1 Terminée
- **Lien :** [Voir le code source](./crypto_ingestion)
- **Documentation :** [📘 Lire la Documentation Technique (PDF)](./crypto_ingestion/docs/documentation.pdf)

*(Prochain projet : Visualisation Power BI ou Transformation avec Databricks)*

## 🏆 Certifications Visées

- [ ] **Microsoft Azure Data Fundamentals (DP-900)** *(En cours de préparation)*
- [ ] **Databricks Lakehouse Fundamentals**
- [ ] **Databricks Data Engineer Associate**
- [ ] **Azure Data Engineer Associate (DP-203)**

---
*Ce portfolio est maintenu par Yoann LEHONG CHEFFSON. N'hésitez pas à explorer le code pour voir ma logique d'ingénierie !*

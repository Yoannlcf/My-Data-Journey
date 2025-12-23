# My-Data-Journey 🚀

Bienvenue sur mon portfolio technique ! 👋

Diplômé en Informatique (BUT & Bachelor UQAC), je consacre actuellement une année de césure à ma spécialisation intensive en **Data Engineering** et **Cloud Computing**.

Ce dépôt centralise mes projets d'apprentissage, mes POCs (Proof of Concepts) et mes pipelines de données, documentant ma progression vers les certifications **Azure** et **Databricks**.

## 🎯 Objectifs & Stack Technique

Mon focus se porte sur la "Modern Data Stack" et l'écosystème Cloud :

| Domaine | Technologies & Outils |
| :--- | :--- |
| **Langages** | 🐍 Python, 🗃️ SQL |
| **Processing** | 🐼 Pandas, 🏹 PyArrow, ⚡ Spark (À venir) |
| **Formats** | 📄 CSV (Bronze), 📦 Parquet (Silver/Gold) |
| **Cloud** | ☁️ Microsoft Azure (Data Lake Gen2, Storage Account) |
| **Architecture** | 🏅 Medallion Architecture (Bronze/Silver/Gold) |
| **Qualité & CI/CD** | 🔐 Dotenv (Sécurité), 🏗️ Git |

## 📂 Projets Réalisés

### 1. Crypto Data Pipeline (Architecture Medallion)
*Pipeline ETL complet : De l'ingestion brute à l'agrégation de KPIs.*

Ce projet implémente une **Architecture Medallion** (standard Databricks) pour traiter des données financières simulées. Il démontre la capacité à transformer des données brutes en insights métier via un pipeline automatisé.

- **Architecture :**
  - **🥉 Couche Bronze (Raw) :** Ingestion de données brutes au format CSV.
  - **🥈 Couche Silver (Cleansed) :** Nettoyage, typage strict et conversion en format **Parquet** (optimisation du stockage et performance de lecture).
  - **🥇 Couche Gold (Aggregated) :** Calcul de KPIs (Moyennes, Totaux) pour usage Business/BI.
  - **🤖 Orchestration :** Script Python maitre pilotant l'exécution séquentielle des tâches ETL.

- **Compétences clés :**
    - **Data Transformation :** Manipulation avancée avec Pandas (Nettoyage, Cast, GroupBy).
    - **Storage Optimization :** Passage du CSV (Row-based) au Parquet (Columnar) pour simuler les bonnes pratiques Big Data.
    - **Sécurité :** Gestion des clés d'accès via variables d'environnement (`.env`).
    
- **Stack :** Python, Pandas, PyArrow, Azure Storage Blob.
- **Statut :** ✅ V1 (Local Pipeline) Terminée
- **Lien :** [Voir le code source](./crypto_ingestion)
- **Documentation :** [📘 Lire la Documentation Technique (PDF)](./crypto_ingestion/docs/Documentation_Pipeline_d_Ingestion_Crypto_vers_Azure_Data_Lake.pdf)

*(Prochaines étapes : Migration vers Azure Data Factory & Visualisation Power BI)*

## 🏆 Certifications Visées

- [ ] **Microsoft Azure Data Fundamentals (DP-900)** *(En cours de préparation)*
- [ ] **Databricks Lakehouse Fundamentals**
- [ ] **Databricks Data Engineer Associate**
- [ ] **Azure Data Engineer Associate (DP-203)**

---
*Ce portfolio est maintenu par Yoann LEHONG CHEFFSON. N'hésitez pas à explorer le code pour voir ma logique d'ingénierie !*

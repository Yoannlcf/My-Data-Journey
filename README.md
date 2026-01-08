# My-Data-Journey 🚀

Bienvenue sur mon portfolio technique ! 👋

Diplômé en Informatique (BUT & Bachelor UQAC), je consacre actuellement une année de césure à ma spécialisation intensive en **Data Engineering** et **Cloud Computing**.

Ce dépôt centralise mes projets d'apprentissage, mes POCs (Proof of Concepts) et mes pipelines de données, documentant ma progression vers les certifications **Azure** et **Databricks**.

## 🎯 Objectifs & Stack Technique

Mon focus se porte sur la "Modern Data Stack" et l'écosystème Cloud :

| Domaine | Technologies & Outils |
| :--- | :--- |
| **Langages** | 🐍 Python, 🗃️ SQL |
| **Processing** | 🐼 Pandas, 🏹 PyArrow, ⚡ Apache Spark (PySpark) |
| **Formats** | 📄 CSV (Bronze), 📦 Parquet (Silver/Gold) |
| **Cloud** | ☁️ Microsoft Azure (Data Lake Gen2, Synapse Analytics, Storage Account) |
| **Architecture** | 🏅 Medallion Architecture (Bronze/Silver/Gold) |
| **Qualité & CI/CD** | 🔐 Dotenv (Sécurité), 🏗️ Git |

## 📂 Projets Réalisés

### 1. Crypto Data Pipeline (Architecture Medallion)
*Pipeline ETL complet : De l'ingestion brute à l'agrégation de KPIs.*

Ce projet implémente une **Architecture Medallion** pour traiter des données financières. Il démontre la capacité à transformer des données brutes en insights métier via un pipeline automatisé.

- **Architecture :**
  - **🥉 Couche Bronze (Raw) :** Ingestion de données brutes au format CSV.
  - **🥈 Couche Silver (Cleansed) :** Nettoyage, typage strict et conversion en format **Parquet**.
  - **🥇 Couche Gold (Aggregated) :** Calcul de KPIs (Moyennes, Totaux) pour usage Business/BI.
  - **🤖 Orchestration :** Script Python maître pilotant l'exécution séquentielle des tâches ETL.

- **Stack :** Python, Pandas, PyArrow, Azure Storage Blob.
- **Lien :** [Voir le code source](./crypto_ingestion)

(Prochaines étapes : Migration vers Azure Data Factory & Visualisation Power BI)

### 2. Exploration Big Data avec Azure Synapse Analytics
*Analyse de données à grande échelle via SQL Serverless et Spark.*

Ce projet démontre l'utilisation d'une plateforme d'analyse intégrée pour ingérer et analyser des données provenant de diverses sources.

- **Réalisations :**
  - **Ingestion de données :** Mise en place de pipelines pour transférer des données depuis des sources HTTP vers un **Azure Data Lake Storage Gen2**.
  - **Analyse SQL Serverless :** Utilisation du **SQL Pool (Built-in)** pour exécuter des requêtes à la demande sur des fichiers CSV via la fonction `OPENROWSET`.
  - **Traitement Spark (Python) :** Configuration d'un **Spark Pool** pour effectuer des tâches de traitement distribué et d'agrégation via des **Notebooks PySpark**.
  - **Visualisation :** Génération de graphiques analytiques directement dans **Synapse Studio**.

- **Stack :** Azure Synapse Analytics, T-SQL, PySpark, Azure Data Lake Gen2.
- **Statut :** ✅ Projet terminé.
- **Lien :** [Voir le code source](./Azure-Synapse-Analysis)

## 🏆 Certifications Visées

- [X] **Microsoft Azure Data Fundamentals (DP-900)** *(En cours de préparation)*
- [ ] **Databricks Lakehouse Fundamentals**
- [ ] **Databricks Data Engineer Associate**
- [ ] **Azure Data Engineer Associate (DP-203)**

---
*Ce portfolio est maintenu par Yoann LEHONG CHEFFSON. N'hésitez pas à explorer le code pour voir ma logique d'ingénierie !*

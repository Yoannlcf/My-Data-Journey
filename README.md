# My-Data-Journey 🚀

Bienvenue sur mon portfolio technique ! 👋

Diplômé en Informatique (BUT & Bachelor UQAC), je consacre actuellement une année de césure à ma spécialisation intensive en **Data Engineering** et **Cloud Computing**. 

Ce dépôt centralise mes projets d'apprentissage, mes POCs (Proof of Concepts) et mes pipelines de données, documentant ma progression vers la majeure Big Data et Machine Learning à l'**Efrei Paris** et l'obtention de mes certifications Cloud.

## 🎯 Objectifs & Stack Technique

Mon focus se porte sur la "Modern Data Stack" et l'écosystème Cloud :

| Domaine | Technologies & Outils |
| :--- | :--- |
| **Langages** | 🐍 Python, 🗃️ SQL |
| **Processing** | 🐼 Pandas, 🏹 PyArrow, ⚡ Apache Spark (PySpark) |
| **Formats** | 📄 CSV (Bronze), 📦 Parquet (Silver/Gold) |
| **Cloud & Infra** | ☁️ Microsoft Azure, 🐋 Docker (Conteneurisation) |
| **BI & Analytics** | 📊 Metabase, 📈 Power BI |
| **Architecture** | 🏅 Medallion Architecture, 🏗️ Git |

## 📂 Projets Réalisés

### 1. Notion Learning Tracker (ETL Pipeline)
*Automatisation du suivi d'apprentissage : De l'API Notion au Dashboard décisionnel.*

Ce projet démontre la mise en place d'un pipeline ETL complet pour centraliser des données d'apprentissage éparpillées. Il met l'accent sur la robustesse du code et l'isolation de l'environnement de visualisation.

- **Réalisations :**
  - **Ingestion :** Extraction automatisée de données via l'**API Notion**.
  - **Transformation :** Nettoyage, normalisation et calculs analytiques (temps de progression) avec **Pandas**.
  - **Stockage :** Persistance des données transformées dans une base **SQLite** structurée.
  - **Visualisation :** Déploiement d'un service de Business Intelligence via **Metabase**.
  - **Infrastructure :** Conteneurisation de la solution avec **Docker** et optimisation de l'environnement réseau **WSL2**.

- **Stack :** Python, Pandas, SQLite, Docker, Metabase, Notion API.
- **Lien :** [Voir le code source](./learning-tracker-etl)



### 2. Crypto Data Pipeline (Architecture Medallion)
*Pipeline ETL complet : De l'ingestion brute à l'agrégation de KPIs.*

Ce projet implémente une **Architecture Medallion** pour traiter des données financières. Il démontre la capacité à transformer des données brutes en insights métier via un pipeline automatisé.

- **Architecture :**
  - **🥉 Couche Bronze (Raw) :** Ingestion de données brutes au format CSV.
  - **🥈 Couche Silver (Cleansed) :** Nettoyage, typage strict et conversion en format **Parquet**.
  - **🥇 Couche Gold (Aggregated) :** Calcul de KPIs (Moyennes, Totaux).
- **Stack :** Python, Pandas, PyArrow, Azure Storage Blob.
- **Lien :** [Voir le code source](./crypto_ingestion)

### 3. Exploration Big Data avec Azure Synapse Analytics
*Analyse de données à grande échelle via SQL Serverless et Spark.*

- **Réalisations :** Ingestion ADLS Gen2, Analyse SQL Serverless via `OPENROWSET`, Traitement distribué via Spark Pool.
- **Stack :** Azure Synapse Analytics, T-SQL, PySpark.
- **Lien :** [Voir le code source](./Azure-Synapse-Analysis)

## 🏆 Certifications

| Certification | Statut | Date |
| :--- | :--- | :--- |
| **Microsoft Certified: Azure Data Fundamentals (DP-900)** | ✅ Obtenue | 8 Janvier 2026 |
| **Azure Data Engineer Associate (DP-203)** | 🎯 Cible | - |

---
*Ce portfolio est maintenu par Yoann LEHONG CHEFFSON. N'hésitez pas à explorer le code pour voir ma logique d'ingénierie !*

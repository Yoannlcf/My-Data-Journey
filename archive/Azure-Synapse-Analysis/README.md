# Analyse de données avec Azure Synapse Analytics

Ce projet fait partie de mon parcours **My-Data-Journey**. J'y démontre la mise en place d'une infrastructure d'analyse de données moderne capable d'ingérer et d'analyser des données massives (Big Data) sur le cloud Microsoft Azure.

## 🛠️ Technologies & Services Azure
* **Azure Synapse Analytics Workspace** : Plateforme d'analyse unifiée pour la gestion des données.
* **Azure Data Lake Storage Gen2** : Système de stockage hiérarchique compatible HDFS pour les charges de travail analytiques.
* **Built-in SQL Pool** : Moteur de requêtes SQL Serverless pour l'exploration de données à la demande.
* **Apache Spark Pool** : Moteur de traitement distribué optimisé pour le calcul en mémoire et le Machine Learning.

## 📈 Réalisations Techniques

### 1. Ingestion de Données (Data Ingestion)
- Configuration d'un pipeline de copie (Copy Data Tool) pour transférer des données produits depuis une source HTTP externe vers le Data Lake.
- Mise en place d'une connexion sécurisée via Integration Runtime.

### 2. Analyse Exploratoire avec SQL (Serverless)
- Utilisation de la fonction `OPENROWSET` pour interroger des fichiers CSV directement dans le stockage, sans importation préalable en base de données.
- Création de requêtes d'agrégation pour résumer les inventaires de produits par catégorie.
- Visualisation immédiate des tendances via l'outil de graphiques intégré à Synapse Studio.

### 3. Analyse de Données avec Spark & Python
- Création d'un pool Spark avec mise à l'échelle automatique (Autoscale).
- Utilisation de **Notebooks PySpark** pour charger des données dans des DataFrames.
- Manipulation et nettoyage des données en Python pour extraire des statistiques clés.

## 📂 Structure des fichiers
* `Azure-Synapse-Analysis/`
    * `Count Products by Category.sql` : Script SQL pour l'analyse à la demande.
    * `Notebook 1.ipynb` : Notebook Python (Spark) pour le traitement des données.
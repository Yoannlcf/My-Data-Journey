# 🛒 Building a Retail Data Pipeline (Walmart Data)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![DataCamp](https://img.shields.io/badge/DataCamp-03E860?style=for-the-badge&logo=datacamp&logoColor=white)](https://www.datacamp.com/)

## 📋 Contexte du Projet
Ce projet implémente un pipeline **ETL (Extract, Transform, Load)** complet pour traiter et consolider les données de ventes de la multinationale Walmart. L'objectif est de centraliser des données provenant de sources hétérogènes pour les rendre exploitables par des équipes d'analystes ou des outils de Business Intelligence.

## 🏗️ Architecture du Pipeline

1. **Extract (Extraction)**
   - Récupération des données transactionnelles depuis un export CSV (simulant une base de données SQL).
   - Récupération de données complémentaires massives stockées au format orienté colonne (`.parquet`).
   - Fusion des sources sur un index commun.

2. **Transform (Transformation & Nettoyage)**
   - **Imputation statistique :** Remplacement des valeurs nulles par la moyenne de la colonne (`CPI`, `Unemployment`, etc.) pour maintenir la cohérence des données.
   - **Feature Engineering :** Typage explicite des dates (`%Y-%m-%d`) et extraction du mois pour faciliter l'agrégation.
   - **Filtrage & Nettoyage :** Conservation exclusive des semaines avec plus de 10 000 $ de ventes et suppression des colonnes inutiles pour optimiser la mémoire.
   - **Agrégation :** Création d'une vue résumée des ventes moyennes par mois via un chaînage de méthodes (method chaining).

3. **Load (Chargement)**
   - Sauvegarde des données nettoyées (`clean_data.csv`) et agrégées (`agg_data.csv`) dans le répertoire de destination, prêtes pour l'analyse.
   - Implémentation d'un système de validation (Fail-Fast) pour s'assurer de l'intégrité des fichiers générés.

## 🚀 Comment exécuter le projet en local

1. Clonez ce dépôt.
2. Assurez-vous d'avoir les données sources (`grocery_sales.csv` et `extra_data.parquet`) dans un sous-dossier `data/`.
3. Lancez le notebook `walmart_retail_pipeline.ipynb` et exécutez les cellules séquentiellement.
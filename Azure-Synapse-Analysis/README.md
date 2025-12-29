# Analyse de données avec Azure Synapse Analytics

Ce projet fait partie de mon parcours **My-Data-Journey**. [cite_start]J'y démontre la mise en place d'un environnement d'analyse moderne (Data Warehouse) capable d'ingérer et de traiter des données à grande échelle[cite: 1, 8].

## 🛠️ Technologies utilisées
* [cite_start]**Azure Synapse Analytics Workspace** : Pour la gestion intégrée de l'analyse[cite: 3, 14].
* [cite_start]**Azure Data Lake Storage Gen2** : Stockage hiérarchique optimisé pour le Big Data[cite: 33, 38].
* [cite_start]**SQL Pool (Built-in)** : Moteur de requêtes SQL à la demande (Serverless)[cite: 4, 191].
* [cite_start]**Apache Spark Pool** : Moteur de traitement distribué pour Python/PySpark[cite: 2, 267].

## 📈 Réalisations techniques
1. **Ingestion de données (Data Ingestion)** : 
   - [cite_start]Création d'un pipeline de copie pour transférer des données produits depuis une source HTTP externe vers le Data Lake[cite: 5, 70, 71, 74].
2. **Analyse Exploratoire avec SQL** : 
   - [cite_start]Utilisation de la fonction `OPENROWSET` pour interroger des fichiers CSV directement dans le Data Lake sans importation préalable[cite: 177, 185].
   - [cite_start]Agrégation des données pour compter les produits par catégorie[cite: 211, 218].
3. **Analyse Big Data avec Spark** : 
   - [cite_start]Chargement des données dans des DataFrames via des **Notebooks PySpark**[cite: 262, 271, 272].
   - [cite_start]Transformation et visualisation des résultats sous forme de graphiques[cite: 280, 308].

## 📂 Structure du projet
* `Count Products by Category.sql` : Script SQL utilisé pour l'analyse à la demande.
* `Notebook 1.ipynb` : Notebook Python contenant les transformations Spark.
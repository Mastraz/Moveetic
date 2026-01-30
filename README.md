# 🎬 Mooveetic : Moteur de Recommandation de Films (TMDB)
Projet d'analyse sémantique de synopsis utilisant le NLP (BERT), la similarité vectorielle et une architecture API (FastAPI). Ce moteur ne se contente pas de chercher des mots-clés : il comprend le sens des histoires pour suggérer des films thématiquement proches.

## 🛠️ Installation et Configuration
Pour garantir le bon fonctionnement du projet, suivez scrupuleusement les étapes ci-dessous.

1. Clonage et Environnement
```Bash
# Cloner le projet
git clone https://github.com/Mastraz/Moveetic.git
cd Projet_Python
```

2. Installation des dépendances
Installez toutes les bibliothèques nécessaires avec une seule commande :

```Bash
pip install -r requirements.txt
```
## 🚀 Utilisation
Le projet est conçu pour être entièrement automatisé. Au premier lancement, il s'occupera de nettoyer les données et de générer les vecteurs mathématiques (Embeddings).

Démarrage du serveur
Lancez l'API avec Uvicorn :

```Bash
python main.py
```
Le serveur sera accessible sur : http://127.0.0.1:8000
---
# Tester l'API

Le moyen le plus simple est d'utiliser l'interface interactive Swagger intégrée :

Ouvrez votre navigateur sur http://127.0.0.1:8000/docs.

Déroulez la route GET /analyze.

Cliquez sur "Try it out".

Entrez un titre et un synopsis (ex: un film de braquage dans l'espace).

Cliquez sur Execute pour voir les 3 meilleures recommandations de la base TMDB.
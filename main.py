import os

import pandas as pd
import uvicorn
from fastapi import FastAPI

from src.movie_cleaner import MovieCleaner
from src.movie_encoder import MovieEncoder
from src.movie_searcher import MovieSearcher


# --- INITIALISATION DE L'API ---
app = FastAPI(
    title="Moveetic API",
    description="Moteur de recommandation basé sur la similarité sémantique."
)
# Utilisation des chemins relatifs vers le dossier /data
CLEANED_CSV = "data/movies_cleaned.csv"
EMBEDDINGS_NPY = "data/synopsis_embeddings.npy"
# Instanciation des composants de traitement
cleaner = MovieCleaner()
encoder = MovieEncoder()

# --- PRÉPARATION DES DONNÉES (PIPELINE) ---

# Étape 1 : Nettoyage du dataset si le fichier propre n'existe pas
if not os.path.exists(CLEANED_CSV):
    cleaner.run_pipeline()

# Étape 2 : Vectorisation de la base si les embeddings sont manquants
if not os.path.exists(EMBEDDINGS_NPY):
    print("[INIT] Première vectorisation de la base de données globale...")
    encoder.vectorize_csv(CLEANED_CSV, output_npy=EMBEDDINGS_NPY)

# Étape 3 : Chargement du moteur de recherche 
# (Obligatoirement après les étapes 1 et 2)
searcher = MovieSearcher(csv_path=CLEANED_CSV, npy_path=EMBEDDINGS_NPY)


# --- ROUTES DE L'API ---

@app.get("/analyze")
def analyze_movie(title: str, synopsis: str):
    """
    Endpoint pour analyser un nouveau film et trouver des recommandations.
    Prend un titre et un synopsis en paramètres.
    """
    # 1. Création du fichier temporaire pour la vectorisation
    temp_file = "data/temp_input.csv"
    user_data = {"title": [title], "overview": [synopsis]}
    pd.DataFrame(user_data).to_csv(temp_file, index=False)
    
    # 2. Transformation du texte en vecteur via le pôle NLP
    query_vector = encoder.vectorize_csv(temp_file)
    
    # 3. Recherche des films similaires via le pôle Algorithmique
    recommendations = searcher.find_similar_movies(query_vector, top_n=3)
    
    # 4. Nettoyage du fichier temporaire (Optionnel)
    if os.path.exists(temp_file):
        os.remove(temp_file)
    
    # 5. Réponse structurée
    return {
        "status": "Success",
        "movie_analyzed": title,
        "recommendations": recommendations
    }


# --- LANCEMENT DU SERVEUR ---
if __name__ == "__main__":
    # Démarrage avec rechargement automatique pour le développement
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
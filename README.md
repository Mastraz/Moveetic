# 🎬💙 Moveetic ! Movies Recommandation 
*Master 1, ISEN, January to February 2026, Teacher: Cyril Barrelet*
Analyzing movie synopses based on user input,
Using : NLP (BERT), Cosine Similarity and an API interface (FastAPI).

## 💽 Setup Tutorial
To ensure the project runs smoothly, please follow the steps below.

### Option 1 : Conda

```Bash
# 1. Clone the project
git clone https://github.com/Mastraz/Moveetic.git
cd Moveetic

# 2. Create the environment from the yml file
conda env create -f environment.yml

# 3. Activate the environment
conda activate Moveetic_env
```

### Option 2 : Pip
Not using Conda ? Make sure you have Python 3.12 installed.

```Bash
# 1. Clone the project
git clone https://github.com/Mastraz/Moveetic.git
cd Moveetic

# 2. Download dependencies
pip install --upgrade pip
pip install -r requirements.txt
```
## 🚀 Using
The project is fully automated. At the first launch, it will clean the data and generate the mathematical vectors (Embeddings).

Starting the server 
Launch the API with Uvicorn :

```Bash
python main.py
```
The server will be accessible at : http://127.0.0.1:8000
---
# API test

The easiest way is to use the built-in Swagger interface : 

Open your browser on : http://127.0.0.1:8000/docs.

Unfold the GET/analyze route.

Click on "Try it out".

Enter a title and a text (ex: a heist movie in space with dogs).

Click on Execute to see the 3 best recommendations from the TMDB database.

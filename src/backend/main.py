# 🚀
from fastapi import FastAPI

# 🐼
import pandas as pd

# 🤓
import joblib
from scipy import sparse
from nltk import PorterStemmer
from sklearn.metrics.pairwise import linear_kernel

# 📦
import string
from pathlib import Path

app = FastAPI()

# As an avid JavaScript enjoyer I'll take every short cut I can to not have to deal with Python file pathing issues 🐍
PROJECT_ROOT = Path(__file__).resolve().parents[2]
ASSETS = PROJECT_ROOT / "assets"

VECT_PATH = ASSETS / "tfidf_vectorizer.joblib"
MATRIX_PATH = ASSETS / "tfidf_matrix.npz"
WINES_PATH = ASSETS / "wines_data.csv"

vectorizer = joblib.load(VECT_PATH)
tfidf_matrix = sparse.load_npz(MATRIX_PATH)
wines_df = pd.read_csv(WINES_PATH)

stemmer = PorterStemmer()


@app.get("/")
def main_route() -> dict[str, str]:
    return {"message": "Hello Wine Enjoyer =)"}

@app.get("/by_description")
def by_description(description: str) -> dict[str, list[dict[str,str]]]:
    translator = str.maketrans("", "", string.punctuation)
    description = description.translate(translator)
    tokens = description.lower().split()
    stemmed = list(map(stemmer.stem, tokens))
    description = " ".join(stemmed)

    tfidf_input = vectorizer.transform([description])
    cosine_sim = linear_kernel(tfidf_input, tfidf_matrix).ravel()
    sim_scores = list(enumerate(cosine_sim))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[0:5]
    results = [
        {
            "title": str(wines_df.iloc[i]["title"]),
            "description": str(wines_df.iloc[i]["description"]),
            "rating_score": str(wines_df.iloc[i]["points"]),
        }
        for i, score in sim_scores
    ]
    return {"results": results}

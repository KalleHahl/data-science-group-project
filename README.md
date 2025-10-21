# [🍷 Pocket Sommelier – Wine Recommender](https://pocket-sommellier.onrender.com/)

**Pocket Sommelier** is a wine recommendation web app built with **FastAPI**.  
It uses **TF-IDF vectorization** of wine descriptions to suggest similar wines based on text similarity.  
All model artifacts are precomputed offline and loaded at runtime for fast responses.

## 🚀 Features

- 🔍 **Content-based recommendations:** Uses TF-IDF + cosine similarity between wine descriptions  
- ⚡ **FastAPI backend:** Simple REST API for querying wine similarities  
- 🧠 **Precomputed artifacts:** TF-IDF vectorizer, sparse matrix, and metadata CSV built via Jupyter Notebook  
- 🐳 **Dockerized environment:** One-command setup for local development  
- 🧩 **Reproducible pipeline:** Notebook for preprocessing and asset generation

## 🧰 Technical Overview

1. **Data Preparation:**  
   - Combine multiple open-source wine datasets  
   - Clean and normalize descriptions  
   - Build TF-IDF model and compute cosine similarity matrix  

2. **Model Artifacts:**  
   - `tfidf_vectorizer.joblib` – serialized scikit-learn vectorizer  
   - `tfidf_matrix.npz` – sparse matrix representation  
   - `wines_data.csv` – metadata (name, country, variety, etc.)

3. **API Endpoints:**

   | Endpoint | Method | Description |
   |-----------|---------|-------------|
   | `/by_description?description=...` | GET | Returns top 5 similar wines to input text |

## 🐳 Quick Start (with Docker)

> These instructions assume you have **Docker** and **docker-compose** installed.

1. **Start the API container:**
   ```bash
   docker-compose up -d
2. **Go to** http://0.0.0.0:8000/

## 🏆 Acknowledgements

### 📊 Datasets
The datasets used in this project are publicly available and were sourced from the following repositories:

- [Wine Ratings Dataset](https://github.com/paiml/wine-ratings/blob/main/wine-ratings.csv)  
- [21st Century Bordeaux Wine Dataset](https://www.kaggle.com/datasets/mexwell/21st-century-bordeaux-wine-dataset)  
- [Wine Reviews Dataset](https://www.kaggle.com/datasets/zynicide/wine-reviews?select=winemag-data-130k-v2.csv)

### 🎨 UI Styling
Parts of the user interface make use of ready-made CSS templates from **[uiverse.io](https://uiverse.io/)**.  
These templates are licensed under the [MIT License](https://opensource.org/licenses/MIT).

- CSS by [0xNihilism (0xNihilist)](https://uiverse.io/profile/0xnihilism) — © 2025 0xNihilism  
- CSS by [Vamsi Devendra Kumar](https://uiverse.io/profile/vamsidevendrakumar) — © 2025 Vamsi Devendra Kumar  

Used with permission under the MIT License.
# 🌌 CineQuest — Movie Recommendation System 🎬

![cinequest banner]

# 🧠 Content-Based Movie Recommender using Flask + TMDb API

CineQuest is a content-based movie recommendation system built with Flask and powered by Natural Language Processing. It analyzes plot similarities to recommend movies, while fetching poster data dynamically using the TMDb API.

# 🔍 Key Features

### 🎬 Movie Selection
Choose any movie and get 5 similar recommendations using cosine similarity.

### 🧠 NLP-Based Recommendation Engine
Built using Bag of Words, stemming, and cosine similarity over TMDB 5000 dataset.

### 🌐 Dynamic Poster Fetching
Uses the TMDb API to display high-quality movie posters.

### ⚙️ Flask Web Interface
Lightweight Python Flask backend with responsive frontend using HTML/CSS.

### 🧪 Jupyter-Based Backend Notebook
All model training and vector generation done in `Movie Recommender System.ipynb`.

---

# 🖼️ Project Demo

## 🎥 Home Page
![🌌 CineQuest - Movie Recommender 1](https://github.com/user-attachments/assets/1080b930-6108-404f-9dd0-f9c5915980e0)


## ✅ Movie Recommendations
![🌌 CineQuest - Movie Recommender 2](https://github.com/user-attachments/assets/cb0307d4-d79b-436a-b039-b9f19aea6bcb)


---

# 🧠 Tech Stack

| Layer          | Tools/Tech Used                         |
|----------------|------------------------------------------|
| Frontend       | HTML, CSS                               |
| Backend        | Python Flask, Jinja2                    |
| ML/NLP         | Pandas, Scikit-learn, NLTK              |
| API Integration| TMDb API (via `requests`)               |
| Deployment     | Localhost (`app.py`)                    |
| Environment    | dotenv for secure API key management    |

---

# 🚀 Setup Instructions

### 1. Clone the Repository

    ```bash

    git clone https://github.com/Aaron-mathew/Cinequest_Movie-Recommendation-System.git

    cd Cinequest_Movie-Recommendation-System
    
    ```

### 2. Generate Required Files

    Open the notebook:
    Backend-notebook/Movie Recommender System.ipynb

    Run all cells to generate:
        movies.pkl
        similarity.pkl

    Move these two files into the root directory (next to app.py).

### 3. Get Your TMDb API Key

    1.Go to TMDb.

    2.Create a free account and request an API Key.

    3.Create a .env file in your root and paste:
        TMDB_API_KEY=your_api_key_here

    .env is auto-ignored in .gitignore.

### 4. Install Requirements
    Recommended to use a virtual environment.

    # Create virtual environment
    python -m venv venv

    # Activate
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate

    # Install dependencies
    pip install -r requirements.txt

### 5. Run the App
        python app.py

    Open in your browser:
    👉 http://127.0.0.1:5000

# Folder Structure

<img width="311" alt="Folder Structure" src="https://github.com/user-attachments/assets/8585912a-1b74-4713-b696-f328cdb55455" />


# 🔑 Insights You’ll Gain

Learn to use NLP for movie similarity scoring

Integrate third-party APIs with Flask

Build full-stack projects using Python alone

Understand practical use of cosine similarity & vectorization

# 📦 Requirements

flask
pandas
requests
python-dotenv
scikit-learn
nltk
numpy

# 🙋‍♂️ Author Info

##👨 Name: Aaron Mathew
##🎓 Branch: CSE-AIDS
##🏫 College: L.N.C.T Bhopal



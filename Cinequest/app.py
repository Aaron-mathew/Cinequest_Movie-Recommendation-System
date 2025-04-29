from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import requests
import traceback
import time
import requests
import os
from dotenv import load_dotenv
    
load_dotenv()

app = Flask(__name__)

movies = pd.read_pickle('movies.pkl')
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDB API
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

movies['title_lower'] = movies['title'].str.lower().str.strip()

def fetch_poster(movie_id, retries=3):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=TMDB_API_KEY&language=en-US"
    for attempt in range(retries):
        try:
            api_key = "YOUR_API_KEY"
            url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_id}"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            poster_path = data['results'][0]['poster_path']
            return "https://image.tmdb.org/t/p/w500" + poster_path
        except Exception as e:
            print(f"[ERROR] Failed TMDB API for: {movie_id}")
            print(e)
            return "data:image/jpeg;base64,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" 
    return "data:image/jpeg;base64,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"

@app.route('/')
def home():
    all_movies = movies['title'].tolist()
    return render_template('index.html', all_movies=all_movies)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    movie = data['movie'].strip().lower()

    print(f"[INFO] Requested movie: '{movie}'")

    try:
        if movie not in movies['title_lower'].values:
            print(f"[WARN] Movie '{movie}' not found in movie list.")
            return jsonify({'recommendations': []})

        movie_index = movies[movies['title_lower'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        for i in movies_list:
            movie_title = movies.iloc[i[0]].title
            poster_url = fetch_poster(movie_title)
            recommended_movies.append({'title': movie_title, 'poster_url': poster_url})

        print(f"[INFO] Sending {len(recommended_movies)} recommendations.")
        return jsonify({'recommendations': recommended_movies})

    except Exception as e:
        print(f"[ERROR] Recommendation failed for '{movie}'")
        traceback.print_exc()
        return jsonify({'recommendations': []})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
import csv 

all_movies = []
with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movie = []
unliked_movie = []
not_watched_movies = []

app = Flask(__name__)

@app.route('/get-movie')

def get_movie():
    movie_data = {
        'title': all_movies[0][19],
        'poster_link': all_movies[0][27],
        'release_date': all_movies[0][13],
        'duration': all_movies[0][15],
        'rating': all_movies[0][20],
        'overview': all_movies[0][9],
    }
    return jsonify({
        'data': movie_data,
        'status': 'success',
    })

@app.route('/liked-movie', methods = ['POST'])

def liked_movie():
    movie = all_movies[0]
    #all_movies = all_movies[1:]
    liked_movie.append(movie)
    all_movies.pop(0)
    return jsonify({
        'status': 'success'
    }), 201

@app.route('/unliked-movie', methods = ['POST'])

def unliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unliked_movie.append(movie)
    return jsonify({
        'status': 'success'
    }), 201

if __name__ == "__main__":
    app.run()
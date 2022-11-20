from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.exceptions import ImproperlyConfigured

from rest_framework.response import Response
from rest_framework.decorators import api_view

import json
import requests
from pathlib import Path

from .models import Movie, Genre
from .serializers import MovieSerializer, MovieListSerializer

BASE_DIR = Path(__file__).resolve().parent.parent
json_file = BASE_DIR / 'secrets.json'

with open(json_file) as s_file:
    secrets = json.load(s_file)


def get_secret(setting, secrets=secrets):

    try:
        return secrets[setting]

    except KeyError:
        error_message = f'{setting} has something wrong'
        raise ImproperlyConfigured(error_message)


BASE_URL = 'https://api.themoviedb.org/3'
API_KEY = secrets["TMDB_API_KEY"]

# Create your views here.


@api_view(['GET'])
def movies_list(request):

    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, tmdb_movie_id):

    if Movie.objects.filter(tmdb_movie_id=tmdb_movie_id).exists():
        movie = get_list_or_404(Movie, tmdb_movie_id=tmdb_movie_id)

    else:
        movie = update_select_movie(tmdb_movie_id)

    serializer = MovieSerializer(movie, many=True)

    return Response(serializer.data)


def update_select_movie(tmdb_movie_id):

    path = f'/movie/{tmdb_movie_id}'

    params = {
        'api_key': API_KEY,
        'region': 'KR',
        'language': 'ko',
    }

    response = requests.get(BASE_URL + path, params=params).json()

    return update_movie(response)


def update_movie(movie_add_db):

    tmdb_movie_id = movie_add_db['id']
    title = movie_add_db['title']
    poster_path = movie_add_db.get('poster_path', '')
    vote_average = movie_add_db['vote_average']
    overview = movie_add_db['overview']

    if Movie.objects.filter(tmdb_movie_id=tmdb_movie_id).exists():

        movie = get_object_or_404(Movie, tmdb_movie_id=tmdb_movie_id)

    else:

        movie = Movie(
            tmdb_movie_id=tmdb_movie_id,
            title=title,
            poster_path=poster_path,
            vote_average=vote_average,
            overview=overview,
        )
        movie.save()

        if movie_add_db.get('genre_ids'):
            genres = movie_add_db['genre_ids']
            for genre_id in genres:
                genre = get_object_or_404(Genre, tmdb_genre_id=genre_id)
                movie.genres.add(genre)

        elif movie_add_db.get('genres'):
            genres = movie_add_db['genres']
            for genre in genres:
                genre_id = genre['id']
                genre = get_object_or_404(Genre, tmdb_genre_id=genre_id)
                movie.genres.add(genre)

    return movie

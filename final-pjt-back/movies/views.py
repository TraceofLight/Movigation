from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.exceptions import ImproperlyConfigured

from rest_framework.response import Response
from rest_framework.decorators import api_view

import json
import requests
from pathlib import Path

from .models import Movie, Genre
from .serializers import MovieSerializer, MovieListSerializer, GenreSerializer

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


def update_movie(each_movie):

    tmdb_movie_id = each_movie['id']
    title = each_movie['title']
    poster_path = each_movie.get('poster_path', '')
    backdrop_path = each_movie.get('backdrop_path', '')
    vote_average = each_movie['vote_average']
    vote_count = each_movie['vote_count']
    overview = each_movie['overview']
    release_date = each_movie.get('release_date')

    if Movie.objects.filter(tmdb_movie_id=tmdb_movie_id).exists():

        movie = Movie.get.objects.filter(tmdb_movie_id=tmdb_movie_id)

    else:

        movie = Movie(
            tmdb_movie_id=tmdb_movie_id,
            title=title,
            poster_path=poster_path,
            backdrop_path=backdrop_path,
            vote_average=vote_average,
            vote_count=vote_count,
            overview=overview,
            release_date=release_date,
        )

        movie.save()

        if each_movie.get('genre_ids'):
            genres = each_movie['genre_ids']
            for genre_id in genres:
                genre = get_object_or_404(Genre, tmdb_genre_id=genre_id)
                movie.genres.add(genre)

        elif each_movie.get('genres'):
            genres = each_movie['genres']
            for genre in genres:
                genre_id = genre['id']
                genre = get_object_or_404(Genre, tmdb_genre_id=genre_id)
                movie.genres.add(genre)

    return movie


@api_view(['GET', 'POST'])
def get_data(request):

    for page in range(1, 21):

        path = '/movie/top_rated'

        params = {
            'api_key': API_KEY,
            'language': 'ko',
            'page': page,
        }

        response = requests.get(BASE_URL + path, params=params).json()

        for each_movie in response['results']:

            try:

                tmdb_movie_id = each_movie['id']
                title = each_movie.get('title')
                poster_path = each_movie.get('poster_path', '')
                backdrop_path = each_movie.get('backdrop_path', '')
                vote_average = each_movie.get('vote_average')
                vote_count = each_movie.get('vote_count')
                overview = each_movie.get('overview')
                release_date = each_movie.get('release_date')

                movie = Movie(
                    tmdb_movie_id = tmdb_movie_id,
                    title = title,
                    poster_path = poster_path,
                    backdrop_path = backdrop_path,
                    vote_average = vote_average,
                    vote_count = vote_count,
                    overview = overview,
                    release_date = release_date,
                )

                movie.save()

                if each_movie.get('genre_ids'):
                    genres = each_movie['genre_ids']
                    for genre_id in genres:
                        genre = Genre.objects.filter(tmdb_genre_id=genre_id)
                        movie.genres.add(genre)

                elif each_movie.get('genres'):
                    genres = each_movie['genres']
                    for genre in genres:
                        genre_id = genre['id']
                        genre = Genre.objects.filter(tmdb_genre_id=genre_id)
                        movie.genres.add(genre)

            except:
                pass

    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def add_genre(request):

    genre_file = BASE_DIR / 'genres.json'

    with open(genre_file, encoding='UTF-8') as g_file:
        genre_data = json.load(g_file)

    for each_genre in genre_data:

        each_genre_data = each_genre['fields']

        tmdb_genre_id = each_genre_data['tmdb_genre_id']
        name = each_genre_data['name']
        like_users = each_genre_data['like_users']

        genre = Genre(
            tmdb_genre_id=tmdb_genre_id,
            name=name,
        )

        genre.save()

        like_users = each_genre_data['like_users']

        for user_id in like_users:
            like_user = Movie.objects.filter(like_users=user_id)
            genre.like_users.add(like_user)

    genres = get_list_or_404(Genre)
    serializer = GenreSerializer(genres, many=True)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def genre_like(request, tmdb_genre_id):
    genre = get_object_or_404(Genre, tmdb_genre_id=tmdb_genre_id)
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        if genre.like_users.filter(pk=request.user.pk).exists():
            genre.like_users.remove(request.user)
        else:
            genre.like_users.add(request.user)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)

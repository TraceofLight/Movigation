from rest_framework import serializers
from .models import Movie, Genre


class MovieSerializer(serializers.ModelSerializer):
    '''
    영화 시리얼라이저
    '''

    class Meta:
        model = Movie
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    '''
    영화 리스트 시리얼라이저
    '''

    class Meta:
        model = Movie
        fields = ('tmdb_movie_id', 'title', 'poster_path', 'vote_average',)


class GenreSerializer(serializers.ModelSerializer):
    '''
    장르 시리얼라이저
    '''

    class Meta:
        model = Genre
        fields = '__all__'

from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movies_list),
    path('<int:tmdb_movie_id>/', views.movie_detail),
    path('<int:tmdb_genre_id>/genre/', views.genre_like),
    # path('getdata/', views.get_data),
    # path('addgenre/', views.add_genre),
]
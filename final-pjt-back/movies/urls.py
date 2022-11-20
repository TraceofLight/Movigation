from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movies_list),
    path('<int:tmdb_movie_id>/', views.movie_detail),
]

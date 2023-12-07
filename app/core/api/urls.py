from django.urls import path

import app.core.api.views

urlpatterns = [
    path('', app.core.api.views.movie_list, name="movie-list"),
    path('<int:pk>/', app.core.api.views.movie_details, name="movie-details"),
]

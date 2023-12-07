from django.urls import path

import app.core.api.views

urlpatterns = [
    path('', app.core.api.views.MovieList.as_view(), name="movie-list"),
    path('<int:pk>/', app.core.api.views.MovieDetails.as_view(), name="movie-details"),
]

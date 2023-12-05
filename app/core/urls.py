from django.urls import path

import app.core.views

urlpatterns = [
    path('list/', app.core.views.movie_list, name="movie-list"),
    path('<int:pk>/', app.core.views.movie_details, name="movie-details"),
]

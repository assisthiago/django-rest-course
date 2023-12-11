from django.urls import path

import app.core.api.views

urlpatterns = [
    path('list/', app.core.api.views.WatchListGAV.as_view(), name="movie-list"),
    path('<int:pk>/', app.core.api.views.WatchListDetails.as_view(), name="movie-details"),
    path('stream/', app.core.api.views.StreamPlataformList.as_view(), name="stream-list"),
    path('stream/<int:pk>/', app.core.api.views.StreamPlataformDetails.as_view(), name="stream-details"),
]

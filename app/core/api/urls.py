from django.urls import path

import app.core.api.views

urlpatterns = [
    path('list/', app.core.api.views.WatchListGAV.as_view(), name="watchlist-list"),
    path('<int:pk>/', app.core.api.views.WatchListDetail.as_view(), name="watchlist-detail"),
    path('stream/', app.core.api.views.StreamPlataformList.as_view(), name="streamplataform-list"),
    path('stream/<int:pk>/', app.core.api.views.StreamPlataformDetail.as_view(), name="streamplataform-detail"),
    path('review/', app.core.api.views.ReviewListGAV.as_view(), name="review-list"),
    path('review/<int:pk>/', app.core.api.views.ReviewDetailGAV.as_view(), name="review-detail"),
]

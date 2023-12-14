from django.urls import include, path
from rest_framework.routers import DefaultRouter

import app.core.api.views

router = DefaultRouter()
router.register("stream", app.core.api.views.StreamPlataformViewSet, basename="streamplataform")

urlpatterns = [
    path('list/', app.core.api.views.WatchListGAV.as_view(), name="watchlist-list"),
    path('<int:pk>/', app.core.api.views.WatchListDetail.as_view(), name="watchlist-detail"),
    path('', include(router.urls)),
    path('stream/<int:pk>/review/', app.core.api.views.ReviewListGAV.as_view(), name="review-list"),
    path('stream/review/<int:pk>/', app.core.api.views.ReviewDetailGAV.as_view(), name="review-detail"),
]

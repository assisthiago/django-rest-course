from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class StreamPlataform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    plataform = models.ForeignKey(
        StreamPlataform, on_delete=models.CASCADE, related_name="watchlist")

    def __str__(self):
        return self.title


class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.rating} stars"

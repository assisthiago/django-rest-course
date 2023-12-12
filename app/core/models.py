from django.db import models


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

import random

from rest_framework import serializers

from app.core.models import StreamPlataform, WatchList


class WatchListSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    def get_rating(self, object):
        return random.randint(0, 5)

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlataformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlataform
        fields = "__all__"

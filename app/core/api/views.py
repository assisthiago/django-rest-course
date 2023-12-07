from django.http import Http404
from rest_framework import status, views, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.core.api.serializers import MovieSerializer
from app.core.models import Movie


class MovieList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class MovieList(views.APIView):
#     def get(self, request, format=None):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, format=None):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetails(views.APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)

        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = MovieSerializer(self.get_object(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        serializer = MovieSerializer(instance=self.get_object(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

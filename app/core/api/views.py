from django.http import Http404
from rest_framework import status, views, generics, mixins
from rest_framework.response import Response

from app.core.api.serializers import ReviewSerializer, StreamPlataformSerializer, WatchListSerializer
from app.core.models import Review, StreamPlataform, WatchList


class WatchListGAV(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class WatchListDetail(views.APIView):
    def get_object(self, pk):
        try:
            return WatchList.objects.get(pk=pk)

        except WatchList.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = WatchListSerializer(self.get_object(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        serializer = WatchListSerializer(instance=self.get_object(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlataformList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    queryset = StreamPlataform.objects.all()
    serializer_class = StreamPlataformSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StreamPlataformDetail(views.APIView):
    def get_object(self, pk):
        try:
            return StreamPlataform.objects.get(pk=pk)

        except StreamPlataform.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = StreamPlataformSerializer(self.get_object(pk=pk), context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        serializer = StreamPlataformSerializer(
            instance=self.get_object(pk=pk),
            data=request.data,
            context={'request': request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewListGAV(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReviewListGAV(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(watchlist=self.kwargs["pk"])

    def perform_create(self, serializer):
        watchlist = WatchList.objects.get(pk=self.kwargs["pk"])
        serializer.save(watchlist=watchlist)


class ReviewDetailGAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

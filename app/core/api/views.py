from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status, views, viewsets, generics, mixins
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


class StreamPlataformViewSet(viewsets.ViewSet):
    queryset = StreamPlataform.objects.all()
    serializer_class = StreamPlataformSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = StreamPlataformSerializer(
            data=request.data,
            context={'request': request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        watchlist = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(watchlist)
        return Response(serializer.data)

    def update(self, request, pk=None):
        serializer = self.serializer_class(
            instance=get_object_or_404(self.queryset, pk=pk),
            data=request.data,
            context={'request': request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        watchlist = get_object_or_404(self.queryset, pk=pk)
        watchlist.delete()
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

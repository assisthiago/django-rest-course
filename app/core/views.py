from django.http import JsonResponse

from app.core.models import Movie


def movie_list(request):
    movies = Movie.objects.all()
    return JsonResponse(data={"data": list(movies.values())})


def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    return JsonResponse(data={
        "name": movie.name,
        "description": movie.description,
        "active": movie.active,
    })

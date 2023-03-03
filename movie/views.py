# from django.http import HttpResponse

# def index(request) :
#     return HttpResponse("Recordando Django")

from .models import Movie
from .serializer import MovieSerializer
from rest_framework import viewsets

# con queryset ya se crea un crud

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    

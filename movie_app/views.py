from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializer import *
from .models import *


# Create your views here.


class DirectorAPIList(ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorAPIRetrieve(RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class MovieAPIList(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieAPIRetrieve(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ReviewAPIList(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewAPIRetrieve(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

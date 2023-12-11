from rest_framework import serializers
from .models import *


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ["id", "name", "movies_count"]


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "director", "all_reviews", "average_rating"]


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"

from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(verbose_name="Директор", max_length=30)

    def __str__(self):
        return self.name

    @property
    def movies_count(self):
        return Movie.objects.filter(director=self).count()


class Movie(models.Model):
    title = models.CharField(verbose_name="Название", max_length=30)
    description = models.TextField(verbose_name="Описание к фильму", blank=True)
    duration = models.SmallIntegerField(
        verbose_name="Длительность фильма",
        validators=[MinValueValidator(limit_value=40, message="Длительность фильма должна быть не менее 30 мин")]
    )
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def average_rating(self):
        reviews = Review.objects.filter(movie=self)

        star_dict = {'*': 1, '**': 2, '***': 3, '****': 4, '*****': 5}

        numeric_ratings = [star_dict[review.rate_stars] for review in reviews if review.rate_stars in star_dict]

        if numeric_ratings:
            return sum(numeric_ratings) / len(numeric_ratings)
        else:
            return None

    @property
    def all_reviews(self):
        reviews = Review.objects.filter(movie=self)
        return [{'id': i.id, 'text': i.text} for i in reviews]


class Review(models.Model):
    STARS = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),

    )
    text = models.TextField(verbose_name="Комментарий")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate_stars = models.CharField(max_length=100, choices=STARS, null=True)

    def __str__(self):
        return self.text
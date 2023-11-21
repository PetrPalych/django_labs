from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(verbose_name="Директор", max_length=30)

    def __str__(self):
        return self.name


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


class Review(models.Model):
    text = models.TextField(verbose_name="Комментарий")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

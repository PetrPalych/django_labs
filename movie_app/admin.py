from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(Director)
class ModelDirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('name', )


@admin.register(Movie)
class ModelMovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'director', )
    list_display_links = ('title',)


@admin.register(Review)
class ModelReviewAdmin(admin.ModelAdmin):
    list_display = ('id', )
    list_display_links = ('id',)

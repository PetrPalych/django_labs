"""
URL configuration for Afisha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie_app.views import *

api_v1 = 'api/v1/'

urlpatterns = [
    path("admin/", admin.site.urls),
    path(api_v1 + "directors", DirectorAPIList.as_view()),
    path(api_v1 + "directors/<int:pk>", DirectorAPIRetrieve.as_view()),
    path(api_v1 + "movie", MovieAPIList.as_view()),
    path(api_v1 + "movie/<int:pk>", MovieAPIRetrieve.as_view()),
    path(api_v1 + "review", ReviewAPIList.as_view()),
    path(api_v1 + "review/<int:pk>", RetrieveAPIView.as_view()),

]

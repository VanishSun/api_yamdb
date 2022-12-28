from django.urls import path, include
from rest_framework import DefaultRouter
from api.views import (
    TitleViewSet,
    CategoryViewSet,
    GenreViewSet
)


app_name = 'api'


v1_router = DefaultRouter()
v1_router.register(r'categories', CategoryViewSet, basename='categories')
v1_router.register(r'genres', GenreViewSet, basename='genres')


urlpatterns = [
    path('', include(v1_router.urls)),

]
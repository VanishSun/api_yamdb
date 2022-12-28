from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters

from reviews.models import Title, Category, Genre
from api.serializers import (
    TitleSerializer,
    CategorySerializer,
    GenreSerializer
)


class CreateListDestroyViewSet(mixins.CreateModelMixin,
                               mixins.ListModelMixins,
                               mixins.ModelMixin,
                               viewsets.GenericViewSet):
    pass


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class CategoryViewSet(CreateListDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    filter_backends = (filters.SearchField, )
    search_fields = ('name', )


class GenreViewSet(CreateListDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    filter_backends = (filters.SearchField, )
    search_fields = ('name', )

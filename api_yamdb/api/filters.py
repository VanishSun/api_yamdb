from django_filters import rest_framework
from reviews.models import Title


class FilterForTitleSet(rest_framework.FilterSet):
    name = rest_framework.CharFilter(field_name='name')
    category = rest_framework.CharFilter(field_name='category__slug')
    genre = rest_framework.CharFilter(field_name='genre__slug')
    year = rest_framework.NumberFilter()

    class Meta:
        model = Title
        fields = ('name', 'category', 'genre', 'year')

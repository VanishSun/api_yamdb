from django.contrib import admin

from .models import Title, Category, Genre


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'year',
        'description',
        'category',
        'genre'
    )
    search_fields = ('name', 'description',)
    list_filter = ('year', )
    empty_value_display = 'None'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )
    search_fields = ('name', 'slug', )
    list_filter = ('name', 'slug', )
    empty_value_display = 'None'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )
    search_fields = ('name', 'slug', )
    list_filter = ('name', 'slug', )
    empty_value_display = 'None'

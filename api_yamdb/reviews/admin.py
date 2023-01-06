from django.contrib import admin

from .models import Title, Category, Genre, Review, Comment


# @admin.register(Title)
# class TitleAdmin(admin.ModelAdmin):
#     list_display = (
#         'name',
#         'year',
#         'description',
#         'category',
#         'genre'
#     )
#     search_fields = ('name', 'description',)
#     list_filter = ('year', )
#     empty_value_display = 'None'


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


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title_id',
        'author',
        'score',
        'pub_date'
    )
    search_fields = ('author', 'title_id', )
    list_filter = ('author', 'score', 'pub_date')
    empty_value_display = 'None'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'review_id',
        'text',
        'pub_date'
    )
    list_filter = ('author', 'pub_date')
    search_fields = ('author', 'review_id', )
    empty_value_display = 'None'

from django.db import models


class Title(models.Model):
    """ Модель, определяющая произведения
    """
    name = models.CharField(max_length=256)
    year = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='categories'
    )
    genre = models.ForeignKey(
        'Genre',
        on_delete=models.CASCADE,
        related_name='genres'
    )


class Category(models.Model):
    """ Модель, определяющая категории
    """
    name = models.CharField(max_length=256, blank=False)
    slug = models.SlugField(blank=False, unique=True)


class Genre(models.Model):
    """ Модель, определяющая жанры
    """
    name = models.CharField(max_length=256, blank=False)
    slug = models.SlugField(blank=False, unique=True)

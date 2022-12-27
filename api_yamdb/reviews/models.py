from django.db import models


class Title(models.Model):
    """ Модель, определяющая произведения
    """
    name = models.CharField(max_length=256)
    year = models.IntegerField()
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='categories'
    )


class Category(models.Model):
    """ Модель, определяющая категории
    """
    name = models.CharField(max_length=256)
    slug = models.SlugField()


class Genre(models.Model):
    """ Модель, определяющая жанры
    """
    name = models.CharField(max_length=256)
    slug = models.SlugField()

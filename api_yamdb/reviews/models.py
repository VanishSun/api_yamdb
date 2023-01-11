from django.contrib.auth import get_user_model
from django.core.validators import (
    MaxLengthValidator,
    MaxValueValidator,
    MinValueValidator,
    RegexValidator
)
from django.db import models

LENGTH_TEXT = 100

User = get_user_model()


class Title(models.Model):
    """ Модель, определяющая произведения."""

    name = models.CharField(
        max_length=256,
        verbose_name="Наименование произведения"
    )
    year = models.IntegerField(verbose_name="Год выпуска")
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание произведения"
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True,
        null=True,
        verbose_name="Категория"
    )
    genre = models.ManyToManyField(
        'Genre',
        through='GenreTitle',
        verbose_name="Жанр"
    )


class Category(models.Model):
    """ Модель, определяющая категории."""

    name = models.CharField(
        max_length=256,
        blank=False,
        validators=[MaxLengthValidator(256)],
        verbose_name="Наименование категории"
    )
    slug = models.SlugField(
        max_length=50,
        blank=False,
        unique=True,
        validators=[
            MaxLengthValidator(50),
            RegexValidator('^[-a-zA-Z0-9_]+$'),
        ],
        verbose_name="Url категории"
    )


class Genre(models.Model):
    """ Модель, определяющая жанры."""

    name = models.CharField(
        max_length=256,
        blank=False,
        validators=[MaxLengthValidator(256)],
        verbose_name="Наименование жанра"
    )
    slug = models.SlugField(
        max_length=50,
        blank=False,
        unique=True,
        validators=[
            MaxLengthValidator(50),
            RegexValidator('^[-a-zA-Z0-9_]+$'),
        ],
        verbose_name="Url жанра"
    )


class GenreTitle(models.Model):
    """ Модель связи жанров и произведений."""

    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    title = models.ForeignKey('Title', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre} {self.title}'


class Review(models.Model):
    """ Модель, определяющая отзывы."""

    text = models.TextField(max_length=256)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='review'
    )
    score = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='review',
        null=True
    )

    class Meta:
        ordering = ('-pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'], name='unique_title_author'
            ),
        ]

    def __str__(self):
        return self.text[:LENGTH_TEXT]


class Comment(models.Model):
    """ Модель, определяющая комментарии."""

    text = models.TextField(
        verbose_name='текст'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:LENGTH_TEXT]

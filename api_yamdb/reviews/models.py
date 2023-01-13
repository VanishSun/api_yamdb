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

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'


class Category(models.Model):
    """ Модель, определяющая категории."""

    name = models.CharField(
        max_length=256,
        validators=[MaxLengthValidator(256)],
        verbose_name="Наименование категории"
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        validators=[
            MaxLengthValidator(50),
            RegexValidator('^[-a-zA-Z0-9_]+$'),
        ],
        verbose_name="Url категории"
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    """ Модель, определяющая жанры."""

    name = models.CharField(
        max_length=256,
        validators=[MaxLengthValidator(256)],
        verbose_name="Наименование жанра"
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        validators=[
            MaxLengthValidator(50),
            RegexValidator('^[-a-zA-Z0-9_]+$'),
        ],
        verbose_name="Url жанра"
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class GenreTitle(models.Model):
    """ Модель связи жанров и произведений."""

    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    title = models.ForeignKey('Title', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre} {self.title}'


class Review(models.Model):
    """ Модель, определяющая отзывы."""

    text = models.TextField(
        max_length=256,
        verbose_name='Текст'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    score = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        verbose_name='Оценка произведения'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата публикации'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )

    class Meta:
        ordering = ('-pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_title_author'
            ),
        ]
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text[:LENGTH_TEXT]


class Comment(models.Model):
    """ Модель, определяющая комментарии."""

    text = models.TextField(
        verbose_name='Текст'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата публикации'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:LENGTH_TEXT]

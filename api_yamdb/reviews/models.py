from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

LENGTH_TEXT = 100

User = get_user_model()


class Title(models.Model):
    """ Модель, определяющая произведения
    """
    name = models.CharField(max_length=256)
    year = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.DO_NOTHING,
        related_name='categories',
        blank=False,
        null=False
    )
    genre = models.ForeignKey(
        'Genre',
        on_delete=models.DO_NOTHING,
        related_name='genres',
        blank=False,
        null=False
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


class Review(models.Model):
    """Класс создания отзывов."""

    text = models.TextField(max_length=256)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='review',
    )
    score = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
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
        verbose_name = 'Отзыв'
        ordering = ('-pub_date',)
        constraints = (
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_author_title'
            ),
        )

    def __str__(self):
        return self.text[:LENGTH_TEXT]


class Comment(models.Model):
    """Класс создания комментариев."""

    text = models.TextField(
        verbose_name='текст'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:LENGTH_TEXT]

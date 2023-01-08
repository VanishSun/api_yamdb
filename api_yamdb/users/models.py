from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, TextField

from .validators import username_validator


USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'
ROLES = [
    (USER, 'user'),
    (MODERATOR, 'moderator'),
    (ADMIN, 'admin')
]


class User(AbstractUser):
    """
    Модель пользователя унаследованная от AbstractUser.
    Добавлены поля роли и биографии.
    Доступные роли: user, moderator и admin. Default - user.
    """
    username = CharField(
        unique=True,
        max_length=150,
        null=False,
        blank=False,
        validators=[
            username_validator,
        ],
        help_text='Имя пользователя. Не более 150 символов',
        verbose_name='Имя пользователя',
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    email = EmailField(
        max_length=254,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Адрес электронной почты',
    )
    first_name = CharField(
        max_length=150,
        blank=True,
        verbose_name='Имя',
    )
    last_name = CharField(
        max_length=150,
        blank=True,
        verbose_name='Фамилия',
    )
    bio = TextField(
        blank=True,
        verbose_name='Биография',
    )
    role = CharField(
        verbose_name='Роль',
        max_length=20,
        choices=ROLES,
        default=USER,
        blank=True
    )
    confirmation_code = CharField(
        max_length=255,
        blank=False,
        null=True,
        default='12345'
    )

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    @property
    def is_admin(self):
        return self.role == ADMIN

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

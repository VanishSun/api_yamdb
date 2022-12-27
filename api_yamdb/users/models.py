from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, TextField


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
    asdf
    """
    username = CharField(
        unique=True,
        max_length=150,
        null=False,
        blank=False,
        help_text='Имя пользователя. Не более 50 символов',
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
    )
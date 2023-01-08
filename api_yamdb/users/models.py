from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import default_token_generator
from django.db.models import CharField, EmailField, TextField
from django.db.models.signals import post_save
from django.dispatch import receiver

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


@receiver(post_save, sender=User, dispatch_uid='create_confirmation_code')
def create_confirmation_code(sender, instance, created, **kwargs):
    if created:
        confirmation_code = default_token_generator.make_token(instance)
        instance.confirmation_code = confirmation_code
        print(instance.confirmation_code)
        instance.save()

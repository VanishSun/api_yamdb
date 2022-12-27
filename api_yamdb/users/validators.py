from django.core.exceptions import ValidationError


def username_validator(value):
    if value == "me":
        raise ValidationError(
            message='Имя пользователя не может быть me!',
            params={'value': value}
        )

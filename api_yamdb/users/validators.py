import re

from django.core.exceptions import ValidationError


def username_validator(value):
    if value == "me":
        raise ValidationError(
            message='Имя пользователя не может быть me!',
            params={'value': value}
        )
    check_value = re.match('^[\\w.@+-]+', value)
    if check_value is None or check_value.group() != value:
        raise ValidationError(
            (f'Недопустимые символы в нике <{value}> '),
            params={'value': value}
        )

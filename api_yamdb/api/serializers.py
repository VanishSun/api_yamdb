from rest_framework import serializers

from users.models import User
from users.validators import username_validator


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )

    def validator_for_username(self, value):
        return username_validator


class GetTokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True)
    confirmation_code = serializers.CharField(
        required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'confirmation_code',
        )


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        max_length=150,
        validators=[
            username_validator,
        ]
    )
    email = serializers.EmailField(
        required=True,
        max_length=254
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )

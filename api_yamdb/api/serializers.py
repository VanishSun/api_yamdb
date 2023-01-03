from rest_framework import serializers, validators

from reviews.models import Category, Genre, Title
from users.models import User
from users.validators import username_validator


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        max_length=150,
        validators=[
            username_validator,
            validators.UniqueValidator(queryset=User.objects.all())
        ]
    )
    email = serializers.EmailField(
        required=True,
        max_length=254,
        validators=[validators.UniqueValidator(queryset=User.objects.all()), ]
    )

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


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        max_length=150,
        validators=[username_validator, ]
    )
    email = serializers.EmailField(
        required=True,
        max_length=254
    )

    class Meta:
        model = User
        fields = ('username', 'email', )


class GetTokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True)
    confirmation_code = serializers.CharField(
        required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code', )


class UserProfileSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        read_only_fields = ('username', 'email', 'role', )


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

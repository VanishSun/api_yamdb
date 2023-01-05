from django.db.models import Avg
from django.core.validators import MaxValueValidator
from django.utils import timezone
from rest_framework import serializers, validators

from reviews.models import (
    Category,
    Comment,
    Genre,
    Review,
    Title
)
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


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug', )


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug', )


class TitleListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'description',
            'rating',
            'category',
            'genre'
        )

    def get_rating(self, obj):
        title = Title.objects.get(pk=obj.id)
        return title.review.aggregate(Avg('score'))['score__avg']


class TitlePostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )
    year = serializers.IntegerField(
        validators=[MaxValueValidator(timezone.now().year)]
    )

    class Meta:
        model = Title
        fields = (
            'name',
            'year',
            'description',
            'category',
            'genre'
        )

    def to_representation(self, value):
        return TitleListSerializer(self.instance).data


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

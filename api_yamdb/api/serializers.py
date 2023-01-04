from rest_framework import serializers, validators

from reviews.models import (
    Category,
    Comment,
    Genre,
    Review,
    Title,
    GenreTitle
)
from users.models import User
from users.validators import username_validator

from django.core.validators import (
    RegexValidator,
    MaxLengthValidator
)


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

    '''def validate_name(self, value):
        if len(value > 256):
            message = 'Превышена допустимая длина'
            serializers.ValidationError(message)
        return value

    def validate_slug(self, value):
        if len(value > 50):
            message = 'Превышена допустимая длина'
            serializers.ValidationError(message)
        return value'''


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug', )


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    genre = GenreSerializer(many=True)

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'description',
            'category',
            'genre'
        )

    def create(self, validated_data):
        p_category = validated_data.pop('category')
        p_genres = validated_data.pop('genre')

        title = Title.objects.create(**validated_data)
        category = Category.objects.get(slug=p_category)

        title.category_id = category.id
        title.save()

        for g in p_genres:
            genre = Genre.objects.get(slug=g)
            GenreTitle.objects.get_or_create(
                genre=genre,
                title=title
            )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

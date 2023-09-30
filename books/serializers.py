from rest_framework import serializers

from users.serializers import UserSerializer

from .models import Author, Genre, BookCondition, PickupLocation, Book, BookRequest


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class BookConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCondition
        fields = '__all__'


class PickupLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickupLocation
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True)
    author = serializers.StringRelatedField()
    condition = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = '__all__'


class BookRequestSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = BookRequest
        fields = '__all__'

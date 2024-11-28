from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Book"""
    
    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ["id", "title", "author", "year"]


class BookCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Book"""
    
    class Meta:
        model = Book
        fields = ["title", "author", "year"]
from rest_framework import generics
from rest_framework.filters import SearchFilter
 
from .models import Book
from .serializers import BookSerializer, BookCreateSerializer


class BookListAPIView(generics.ListAPIView):
    """Представление для вывода списка книг"""
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("title", "author", "year")


class BookCreateAPIView(generics.CreateAPIView):
    """Представления добавления книги"""
    
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Представление изменения статуса книги"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer

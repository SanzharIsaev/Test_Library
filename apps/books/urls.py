from django.urls import include, path
from rest_framework import routers

from . import views

urlpatterns = [
    path("", views.BookListAPIView.as_view(), name="book_list"),
    path("create/", views.BookCreateAPIView.as_view(), name="book_create"),
    path("<int:pk>/", views.BookRetrieveUpdateDestroyAPIView.as_view(), name="book_detail"),
]
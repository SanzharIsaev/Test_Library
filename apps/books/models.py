from django.db import models


class Book(models.Model):
    """Модель книг"""

    STATUS_CHOICES = [
        ("В наличии", "В наличии"),
        ("Выдана", "Выдана"),
    ]

    title = models.CharField(
        max_length=100,
        verbose_name="Название книги"
    )

    author = models.CharField(
        max_length=200,
        verbose_name="Автор книги"
    )
    
    year = models.PositiveIntegerField(
        verbose_name="Дата издания книги"
    )
    
    status = models.CharField(
        max_length=9,
        choices=STATUS_CHOICES,
        default="В наличии",
        verbose_name="Статус книги"
    )
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги" 

    def __str__(self):
        return self.title

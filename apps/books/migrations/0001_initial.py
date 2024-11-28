# Generated by Django 5.1.3 on 2024-11-28 07:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Название книги"),
                ),
                (
                    "author",
                    models.CharField(max_length=200, verbose_name="Автор книги"),
                ),
                (
                    "year",
                    models.PositiveIntegerField(verbose_name="Дата издания книги"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("В наличии", "В наличии"), ("Выдана", "Выдана")],
                        default="В наличии",
                        max_length=9,
                        verbose_name="Статус книги",
                    ),
                ),
            ],
            options={
                "verbose_name": "Книга",
                "verbose_name_plural": "Книги",
            },
        ),
    ]
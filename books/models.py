from django.db import models
from django.db.models import CASCADE


class Writer(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=250,)
    last_name = models.CharField(verbose_name="Last Name", max_length=250,)

    class Meta:
        verbose_name: str = "Writer"
        verbose_name_plural: str = "Writers"


class Genre(models.Model):
    name = models.CharField(verbose_name="Name", max_length=250,)

    class Meta:
        verbose_name: str = "Genre"
        verbose_name_plural: str = "Genres"


class Book(models.Model):
    name = models.CharField(verbose_name="Name", max_length=250,)
    writer = models.ForeignKey(verbose_name="Writer", to=Writer, on_delete=CASCADE,)
    synopsis = models.TextField(verbose_name="Synopsis", max_length=5000,)
    genre = models.ForeignKey(verbose_name="Genre", to=Genre, on_delete=CASCADE)
    release_date = models.DateTimeField(verbose_name="Release Date")
    price = models.PositiveBigIntegerField(verbose_name="Price")

    class Meta:
        verbose_name: str = "Book"
        verbose_name_plural: str = "Books"

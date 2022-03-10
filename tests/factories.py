from factory.django import DjangoModelFactory
import factory

from books.models import Writer, Genre, Book


class WriterFactory(DjangoModelFactory):
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    class Meta:
        model = Writer


class GenreFactory(DjangoModelFactory):
    name = factory.Faker("name")

    class Meta:
        model = Genre


class BookFactory(DjangoModelFactory):
    name = factory.Faker("name")
    writer = factory.SubFactory(WriterFactory)
    synopsis = factory.Faker("text")
    release_date = factory.Faker("date_time")
    price = factory.Faker("random_int")
    genre = factory.SubFactory(GenreFactory)

    class Meta:
        model = Book

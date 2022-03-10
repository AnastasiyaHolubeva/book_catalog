from django.forms import model_to_dict
from django.test import TestCase
from django.urls import reverse

from tests.factories import BookFactory, WriterFactory, GenreFactory


class BookListTests(TestCase):
    def test_book_create(self):
        writer = WriterFactory.create()
        genre = GenreFactory.create()
        book = BookFactory.build()
        book_dict = model_to_dict(book)
        book_dict.pop("id")
        book_dict["writer"] = writer.id
        book_dict["genre"] = [genre.id]
        response = self.client.post(reverse("books:book-list"), data=book_dict)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(writer.last_name, response.data["writer"]["last_name"])

    def test_book_list(self):
        BookFactory.create_batch(10)
        response = self.client.get(reverse("books:book-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 10)

    def test_book_genre_filter(self):
        genre1 = GenreFactory.create()
        genre2 = GenreFactory.create()
        book1 = BookFactory.create(genre=genre1)
        book2 = BookFactory.create(genre=genre2)
        # Create batch of 10 random books
        BookFactory.create_batch(10)
        response = self.client.get(
            reverse("books:book-list"),
            data={"genre__name__in": ",".join([genre1.name, genre2.name])},
        )
        book_ids = [book["id"] for book in response.data]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(book_ids, [book1.id, book2.id])

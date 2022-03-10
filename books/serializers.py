from rest_framework import serializers

from books.models import Book, Writer, Genre


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = [
            "id",
            "first_name",
            "last_name",
        ]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = [
            "id",
            "name",
        ]


class BookSerializer(serializers.ModelSerializer):
    def to_representation(self, instance: Book) -> Book:
        self.fields["genre"] = GenreSerializer()
        self.fields["writer"] = WriterSerializer()
        return super().to_representation(instance)

    class Meta:
        model = Book
        fields = [
            "id",
            "writer",
            "name",
            "synopsis",
            "genre",
            "release_date",
            "price",
        ]

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from books.models import Book, Writer
from books.serializers import BookSerializer, WriterSerializer


class WriterViewSet(viewsets.ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
    )
    filterset_fields = {
        "genre__name": ("in", "exact"),
        "price": ("gte", "lte"),
    }
    search_fields = (
        "name",
        "writer__first_name",
        "writer__second_name",
        "genre__name",
    )

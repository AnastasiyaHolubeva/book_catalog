from django.urls import path

from books.views import BookViewSet

app_name = "books"

urlpatterns = [
    path(
        "books/",
        BookViewSet.as_view({"get": "list", "post": "create",}),
        name="book-list",
    ),
    path(
        "books/<slug:pk>/", BookViewSet.as_view({"get": "retrieve"}), name="book-detail"
    ),
]

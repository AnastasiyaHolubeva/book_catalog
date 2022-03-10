from django.contrib import admin

from books.models import Book, Writer, Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "writer_name")

    @admin.display(description="Writer Name")
    def writer_name(self, obj):
        return f"{obj.writer.first_name} {obj.writer.last_name}"

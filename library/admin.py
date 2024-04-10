from django.contrib import admin
from .models import Book, Author, Bookings, Comment
from import_export.admin import ImportExportModelAdmin


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ("id", 'title', 'description_wivshow', 'price', 'coment_count', 'count', 'author')
    list_display_links = ("id", 'title', 'description_wivshow', 'price', 'coment_count', 'count', 'author')
    search_fields = ('title', "id")
    ordering = ('id', "title")
    autocomplete_fields = ('author',)

    def description_wivshow(self, obj):
        return obj.description[:20]

    def coment_count(self, obj):
        return obj.coment.all().count()


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ("id", 'first_name', 'last_name')
    list_display_links = ("id", 'first_name', 'last_name')
    search_fields = ("id", 'first_name', "last_name")
    ordering = ('id', "first_name")


@admin.register(Bookings)
class BookingsAdmin(ImportExportModelAdmin):
    list_display = ("id", 'take', 'return_date')
    list_display_links = ("id", 'take', 'return_date')
    search_fields = ("id",)
    ordering = ('id', "take")


@admin.register(Comment)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ("id", 'text', 'student')
    list_display_links = ("id", 'text', 'student')
    search_fields = ("id", "text")
    ordering = ("id",)

from django.contrib import admin
from .models import Student, Address
from import_export.admin import ImportExportModelAdmin


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'status', 'age', 'address')
    list_display_links = ('id', 'first_name', 'last_name', 'status', 'age', 'address')
    search_fields = ('first_name', 'id')
    ordering = ('id', "first_name")


@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    list_display = ("id", 'name',)
    list_display_links = ("id", 'name',)
    search_fields = ("id", "name")
    ordering = ('id', "name")

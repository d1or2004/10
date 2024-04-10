from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get('search')
        if not search:
            books = Book.objects.all()
            context = {
                'books': books,
                'search': search
            }
            return render(request, 'library.html', context)
        else:
            books = Book.objects.filter(title_icontains=search)
            context = {'books': books,
                       'search': search}
            return render(request, 'library.html', context)


class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        return render(request, 'book_datail.html', {'book': book})

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy

from .models import Book
from .forms import BookForm


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'landing/book_creation.html'
    success_url = reverse_lazy('book-list')


class BookListView(ListView):
    template_name = 'landing/book_list.html'
    model = Book
    context_object_name = 'books'

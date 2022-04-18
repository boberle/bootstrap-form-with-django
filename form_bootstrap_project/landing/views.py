from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.urls import reverse_lazy

from .models import Book
from .forms import BookForm


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'landing/book_creation.html'
    success_url = reverse_lazy('book-list')

    def get(self, *args, **kwargs):
        ans = super().get(*args, **kwargs)
        #print(ans.context_data)
        for field in ans.context_data['form']:
            print("FIELD", type(field), str(field), dir(field), field.field)
        return ans

    def render_to_response(self, context, **response_kwargs):
        ans = super().render_to_response(context, **response_kwargs)
        #print(dir(ans))
        return ans


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'landing/book_creation.html'
    success_url = reverse_lazy('book-list')

    def get(self, *args, **kwargs):
        ans = super().get(*args, **kwargs)
        print(ans.context_data)
        return ans

    def render_to_response(self, context, **response_kwargs):
        ans = super().render_to_response(context, **response_kwargs)
        print("RENDER_TO_RESPONSE", ans.context_data)
        return ans


class BookListView(ListView):
    template_name = 'landing/book_list.html'
    model = Book
    context_object_name = 'books'

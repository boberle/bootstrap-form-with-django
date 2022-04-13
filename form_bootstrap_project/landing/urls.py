from django.urls import path

from .views import BookCreateView, BookListView

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("new/", BookCreateView.as_view(), name="new-book"),
]

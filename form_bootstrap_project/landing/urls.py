from django.urls import path

from .views import BookCreateView, BookListView, BookUpdateView

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("new/", BookCreateView.as_view(), name="new-book"),
    path("edit/<int:pk>/", BookUpdateView.as_view(), name="update-book"),
]

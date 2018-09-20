from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.exceptions import PermissionDenied
from .models import Book


def book_list_view(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    books = Book.objects.filter(user_id__username=request.user.username)

    context = {
        'books': books
    }

    return render(request, 'books/book_list.html', context)


def book_detail_view(request, pk=None):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))

    book = get_object_or_404(Book, id=pk, user_id__username=request.user.username)

    context = {
        'book': book,
    }

    return render(request, 'books/book_detail.html', context)

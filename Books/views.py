from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Book
from django.db.models import Q
from .forms import BookForm


# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/detail.html', {'book': book})


def search_books(request):
    filter_by = request.GET.get('filter_by', 'title')
    query = request.GET.get('query', '')

    if filter_by == 'title':
        books = Book.objects.filter(title__icontains=query)
    elif filter_by == 'author':
        books = Book.objects.filter(author__icontains=query)
    elif filter_by == 'genre':
        books = Book.objects.filter(genre__name__icontains=query)
    elif filter_by == 'id':
        books = Book.objects.filter(id=query)

    return render(request, 'books/search_books.html', {'books': books})

def add_book(request):
    submitted = False
    if request.method == 'POST': 
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('book:add_book') + '?submitted=True')
    else:
        form = BookForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'books/add_book.html', {'form': form, 'submitted': submitted})

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect("book:index")
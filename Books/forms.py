from django import forms
from django.forms import ModelForm
from .models import Book


# Create your book forms here.

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'location')
        labels = {'title': '', 'author': '', 'genre': '', 'location':''}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'genre': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Genre'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
        }
        

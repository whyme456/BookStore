from django.db import models
from tastypie.resources import ModelResource
from Books.models import Book
# Create your models here.

class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'books'
        excludes = ['date_created',]
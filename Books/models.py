from django.db import models
from django.utils import timezone



# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    location = models.CharField(max_length=2)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title



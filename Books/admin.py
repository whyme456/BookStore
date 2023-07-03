from django.contrib import admin
from .models import Genre, Book
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','name')

    
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','genre')
    exclude = ('date_created',)

admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)



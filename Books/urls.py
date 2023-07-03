from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
    path('search_books/', views.search_books, name='search_books'),
    path('add_book/', views.add_book, name='add_book'),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete_book"),

]

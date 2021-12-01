from django.urls import path
from django.contrib import admin


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('admin/', admin.site.urls, name='admin'),

    path('add_new_book/', views.libraryFunction, name='add_new_book'),
    path('view_books/', views.dataviewfunction, name='view_books'),
    path('delete/<int:book_id>/', views.deletefunction, name='delete_book'),

    # path('delete_book/', views.deletefunction, name='delete_book'),


]
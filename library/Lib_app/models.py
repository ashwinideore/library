from django.db import models
from django import forms


class library (models.Model):
    book_id = models.IntegerField(max_length=20)
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)

    class Meta:
        db_table='library_books_info'

class libraryForms(forms.ModelForm):
    book_id = forms.IntegerField()
    book_name = forms.CharField(max_length=100)
    book_author = forms.CharField(max_length=100)

    # class Meta:
    #     model = 'library'
    #     fields = '__all__'


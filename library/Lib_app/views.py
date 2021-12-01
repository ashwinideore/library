from django.shortcuts import render, redirect
from .models import library, libraryForms
# from .models import library

from django.http import HttpResponse


def index(request):
    return render(request, 'welcome_page.html')


def libraryFunction (request):

    if request.method=="POST":
        form = libraryForms(request.POST)
        if form.is_valid():
            print('test1')
            try:
                print('test2')

                form.save()
                return redirect('view_books')
                # return HttpResponse('form saved')

            except:
                pass
    else:
        print('test4')

        form = libraryForms()
        context = {
            'form': form
        }
        return render(request, 'library_index.html', context)



def dataviewfunction(request):
    print(1)
    bookObject = library.objects.all()
    print('bookObject', bookObject)

    context = {
        'bookObject':bookObject
    }
    return render(request, 'viewbooksdata.html', context)

def deletefunction(request, book_id):

    book = library.objects.get(id=book_id)
    library.delete(book)
    return redirect('view_books')



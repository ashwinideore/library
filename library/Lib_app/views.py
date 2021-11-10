from django.shortcuts import render
from library.Lib_app.models import library, libraryForms

def libraryFunction (request):
    if request.method=="POST":
        form = libraryForms(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                pass
    else:
        form = libraryForms()
        context = {
            'form':form
        }
    return render(request, 'library_index.html', context)
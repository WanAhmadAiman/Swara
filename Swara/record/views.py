#from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Entryform
from .models import Entry
from django.views.generic import CreateView

def record(request):
    return render(request, 'record/record.html')

def submit(request):

    if request.method== 'POST':
        form = Entryform(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            saved = True
            return render(request,'record/saved.html')
        else:
            print (form.errors)
            saved = False
    else:
        form = Entryform()

    contextdict = {"form": form}
    return render(request, 'record/saved.html', contextdict)

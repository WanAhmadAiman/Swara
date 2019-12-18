from django.http import HttpResponse
from django.shortcuts import render

def manageaccount(request):
    return render(request, 'accounts/manageaccount.html')

def profilepage(request):
    return render(request, 'accounts/profilepage.html')

def signup(request):
    return render(request, 'accounts/signup.html')
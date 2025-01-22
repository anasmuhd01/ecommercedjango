from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def create(request):
    return render(request,'create.html')

def list(request):
    return render(request, 'list.html')

def edit(request):
    return render(request, 'edit.html')


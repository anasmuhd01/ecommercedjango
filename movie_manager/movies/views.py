from django.shortcuts import render
from django.http import HttpResponse
from . models import MovieInfo
# Create your views here.

def create(request):
    if request.POST:
        # this print what is POST ed from the fornt end # print(request.POST)
        # This is used to print what is you needed # print(request.POST.get('title'))
        title = request.POST.get('title')
        year = request.POST.get('year')
        desc = request.POST.get('description')        
        movie_obj = MovieInfo(title=title, year=year, description=desc)  
        movie_obj.save()
    return render(request,'create.html')

def list(request):
    movie_list ={
        'movies':[
            {
        'title':'Godfather',
        'year':'1999',
        'summary':'a nice movie',
        'img':'Logo.png',
        'success': True

    },{
        'title':'Hector solomonka',
        'year':'2010',
        'summary':'a  movie about solomonka',
        'img':'Logo.png',
        'success': False
        
    },{
        'title':'willian arc',
        'year':'2020',
        'summary':'a villian movie',
        'img':'Logo.png',
        'success': True
        
    }
    ]
    }
    return render(request, 'list.html',movie_list)

def edit(request):
    return render(request, 'edit.html')


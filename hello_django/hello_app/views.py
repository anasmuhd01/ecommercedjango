from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def printHelo(request):
    movie_list ={
        'movies':[
            {
        'title':'Godfather',
        'year':'1999',
        'summary':'a nice movie',
        'success': True

    },{
        'title':'Hector solomonka',
        'year':'2010',
        'summary':'a  movie about solomonka',
        'success': False
        
    },{
        'title':'willian arc',
        'year':'2020',
        'summary':'a villian movie',
        'success': True
        
    }
    ]
    }
    return render(request,'hello.html',movie_list)

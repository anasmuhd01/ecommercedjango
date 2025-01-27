from django.shortcuts import render
from django.http import HttpResponse
from . models import MovieInfo
from .forms import MovieForm
# Create your views here.

def create(request):
    # frm = MovieForm()
    # if request.POST:
    #     # this print what is POST ed from the fornt end # print(request.POST)
    #     # This is used to print what is you needed # print(request.POST.get('title'))
    #     title = request.POST.get('title')
    #     year = request.POST.get('year')
    #     desc = request.POST.get('description')        
    #     movie_obj = MovieInfo(title=title, year=year, description=desc)  
    #     movie_obj.save()
    # return render(request,'create.html', {'frm':frm})
    # Another way is
    if request.POST:
        frm = MovieForm(request.POST)
        if frm.is_valid:
            frm.save()
    else:
        frm = MovieForm()

    return render(request,'create.html', {'frm':frm})

def list(request):
    movie_list = MovieInfo.objects.all() # Accessing model MovieInfo and -> movie_list then step 19
    print(movie_list)
    return render(request, 'list.html',{'movies':movie_list})

def edit(request):
    return render(request, 'edit.html')


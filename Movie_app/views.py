from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth.decorators import login_required
from .forms import MovieUpdateForm
from .models import Movie
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def index(request):
    
    data = Movie.objects.all()
    
    return render(request,'index.html',{'data':data})
    
    
def about(request):
    return render(request,'about-us.html')
def articles(request):
    return render(request,'articles.html')
def contact(request):
    return render(request,'contact-us.html')
def sitemap(request):
    return render(request,'sitemap.html')

def create1(request):
    frm = MovieUpdateForm()
    if request.POST:
        frm = MovieUpdateForm(request.POST,request.FILES)
        
        if frm.is_valid():
            frm.save()
            return redirect('view')
        
    else:
        frm=MovieUpdateForm()
    return render(request,'create.html',{'frm':frm})

@login_required(login_url='/login/')
def view(request):
    data = Movie.objects.all()
    
    return render(request,'view.html',{'data':data})


from .models import Movie
from .forms import MovieUpdateForm

def update_movie(request, id):
    instance_update = Movie.objects.get(id=id)
    if request.POST:
        frm = MovieUpdateForm(request.POST,instance = instance_update)
        if frm.is_valid():
            instance_update.save()
    else:
        frm = MovieUpdateForm(instance=instance_update)
    return render(request,'create.html',{'frm':frm})

def delete_movie(request, id):
    instance = Movie.objects.get(id=id)
    instance.delete()
    movie_data_set = Movie.objects.all()
    return render(request,'view.html',{'data':movie_data_set})



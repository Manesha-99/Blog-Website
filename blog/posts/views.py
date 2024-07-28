from django.shortcuts import render
from .models import Posts

def index(request):
    posts = Posts.objects.all()
    return render(request,'index.html', {'posts' : posts})

def posts(request, pk):
    post = Posts.objects.get(id=pk)
    return render(request,'posts.html',{'post' : post})
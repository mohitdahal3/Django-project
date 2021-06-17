from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def bloghome(request):
    allposts = Post.objects.all()
    context = {
        'allposts' : allposts
    }
    return render(request , 'blog/home.html' , context)


def blogpost(request , slug):
    post = Post.objects.get(sno = int(slug))
    
    return render(request , 'blog/blogpost.html' , {'post':post})
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Post , Blogcomment
from django.contrib import messages
# Create your views here.
def bloghome(request):
    allposts = Post.objects.all()
    context = {
        'allposts' : allposts
    }
    return render(request , 'blog/home.html' , context)


def blogpost(request , slug):
    post = Post.objects.get(sno = slug) 
    comment = Blogcomment.objects.all().filter(post = post)
    return render(request , 'blog/blogpost.html' , {'post':post , 'comments':comment})


def postcomment(request):
    if request.method == "POST":
        postid = request.POST.get('postid' , '')
        try:
            user = request.user
            print(user,type(user))
            pcomment = request.POST.get('comment' , '')
            if( not len(pcomment)>0):
                raise Exception('Comment field must not be blank!')
            if user.id == None:
                messages.error(request , 'Login or Signup first to be able to add comments')
                return redirect(f"/blog/{postid}")
            post = Post.objects.get(sno = postid)
            comment = Blogcomment(comment=pcomment , user = user , post = post)
            comment.save()
            messages.success(request , 'Comment added successfully!')
            return redirect(f"/blog/{postid}/")   
        except Exception as e:
            messages.error(request , "Comment not added")
            return redirect(f"/blog/{postid}")
    return HttpResponse("bad request")
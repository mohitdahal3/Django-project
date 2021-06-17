from django.shortcuts import render , HttpResponse
from django.contrib import messages
from .models import Contact
from blog.models import Post
# Create your views here.
def home(request):
    allposts = Post.objects.all()
    
    context = {
        'allposts' : allposts[len(allposts)-3:len(allposts)]
    }
    return render(request , 'home/home.html' , context)


def contact(request):
    # messages.error(request , "this is a success message")
    if request.method == 'POST':
        name = request.POST.get('name' , '')
        email = request.POST.get('email' , '')
        phone = request.POST.get('phone' , '')
        message = request.POST.get('message' , '')
        if len(name) <2 or len(email)<3 or len(phone) < 10 or len(message)<3:
            messages.error(request , "Your message has not been sent. Try changing the values!")
        else:
            con = Contact(name = name , email = email , phone = phone , message = message)
            con.save()
            
            messages.success(request , "Your message has been sent!")
        return render(request , 'home/contact.html')
    return render(request , 'home/contact.html')


def about(request):
    return render(request , 'home/about.html')

def search(request):

    query1 = request.GET.get('query' , '')
    query = query1.lower()
    allposts = Post.objects.all()
    posts = []
    for post in allposts:
        if query in post.title.lower() or query in post.author.lower() or query in post.content.lower():
            posts.append(post)
        
    return render(request,'home/search.html' , {'allposts' : posts , 'query':query1})
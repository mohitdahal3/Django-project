from django.shortcuts import render , HttpResponse , redirect
from django.contrib import messages
from .models import Contact
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User 
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

def handlesignup(request):
    if request.method == "POST":
        try:
            firstname = request.POST.get('firstname' , '')
            lastname = request.POST.get('lastname' , '')
            email = request.POST.get('email' , '')
            password1 = request.POST.get('password1' , '')
            password2 = request.POST.get('password2' , '')
            uname = request.POST.get('uname' , '')
            if(password1 != password2):
                messages.error(request , 'Two password fields did not match! Try again')
            elif not uname.isalnum():
                messages.error(request , 'Username must be alphanumeric (not including punctuations like !@#$%^&*()_+-=). Try again')                
            elif len(uname) > 70:
                messages.error(request , 'Username is too long. Try again')                
            else:
                user = User.objects.create_user(uname , email , password1)
                user.first_name = firstname
                user.last_name = lastname
                user.save()
                messages.success(request , 'Your account has been sucessfully created!')

        except Exception as e:
            messages.error(request , "There has been some error! Account not created. Try using different keywords")  
            
            return redirect('/') 
    else:
        messages.error(request , "There has been some error!")  
        return redirect('/')
    return HttpResponse('bad request')  



def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST.get('luname' , '')
        loginpassword = request.POST.get('lpassword1' , '')
        user = authenticate(username=loginusername , password = loginpassword)
        if user is not None:
            login(request , user)
            
            messages.success(request , "You are sucessfully logged in!")
            return redirect('/')
        else:
            messages.error(request , "Login failed!")    
            return redirect('/')

    return HttpResponse('bad request')   


def handlelogout(request):
    if request.method == "POST":
        try:
            logout(request)
            messages.success(request , "You are successfully logged out")
            return redirect('/')
        except:
            messages.error(request , "There has been some error!")    
            return redirect('/')
    return HttpResponse('bad request')    
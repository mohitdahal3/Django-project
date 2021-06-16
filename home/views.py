from django.shortcuts import render , HttpResponse
from django.contrib import messages
from .models import Contact
# Create your views here.
def home(request):
    return render(request , 'home/home.html')


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
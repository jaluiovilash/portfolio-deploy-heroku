from django.shortcuts import render, redirect
from django.contrib import messages

from portfolio.models import Contact, Blogs

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def resume(request):
    return render(request,'resume.html')

def projectPortfolio(request):
    return render(request,'projectPortfolio.html')

def services(request):
    return render(request,'services.html')


def contact(request):
    if request.method == "POST":
        username = request.POST.get('username') 
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        description = request.POST.get('description')

        query=Contact(username=username,email=email,subject=subject,description=description)
        query.save()

        messages.success(request, 'Your message has been sent successfully...!')
        return redirect('/contact/')

    return render(request, 'contact.html')


def blog(request):
    posts=Blogs.objects.all().order_by('-timeStamp')
    context={"posts":posts}
    return render(request,'blog.html',context)




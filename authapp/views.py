from django.shortcuts import render

# Create your views here.
def signup(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_pass1 = request.POST.get('pass1')
        get_pass2 = request.POST.get('pass2')
        print(get_email)
        print(get_pass1)
        print(get_pass2)
        
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')
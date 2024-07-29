from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def signup(request):
    if request.method == "POST":
        get_username = request.POST
        get_email = request.POST.get('email')
        get_pass1 = request.POST.get('pass1')
        get_pass2 = request.POST.get('pass2')
        username = get_email

        if get_pass1 != get_pass2:
            messages.info(request, 'Passwords do not match...!')
            return redirect('/auth/signup/')

        try:
            if User.objects.get(username=get_email):
                messages.warning(request, "Email already exists...!")
                return redirect('/auth/signup/')
        except User.DoesNotExist:
            pass

        user = User.objects.create_user(username=username, email=get_email, password=get_pass1)
        user.save()
        messages.success(request, 'User is created. Please login...!')
        return redirect('/auth/login/')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successfully done...!')
            return redirect('/')  # Redirect to a home page or dashboard
        else:
            messages.error(request, 'Invalid credentials...!')
            return redirect('/auth/login/')

    return render(request, 'login.html')

def logout_view(request):
    auth_logout(request)
    messages.success(request,"Logout successfully...!")
    return redirect('/auth/login/')

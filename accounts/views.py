from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def register_view(request):
    if request.method == "GET":
        return render (request, 'auth/register.html')
    elif request.method == 'POST':
        username = request.POST.get("username", False)
        email = request.POST.get("email", False)
        password = request.POST.get("password", False)
        confirm_password = request.POST.get("confirm_passowrd",False)
        if not username or not email or not password or not confirm_password:
            return HttpResponse("Please fill all datas")
        if not password == confirm_password:
            return render (request, 'auth/register.html')
        user = User.objects.filter(username = username).exists()
        if user:
            return HttpResponse("User already exists")
        new_user = User.objects.create_user(
            username=username,
            email=email
        )
        new_user.set_password(password)
        new_user.save()
        return redirect('login')
    

def login_view(request):
    if request.method == "GET":
        return render(request, 'auth/login/html')
    elif request.method == "POST":
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        if not username or not password:
            return render(request, 'auth/login.html')
        user = authenticate(request, 
                            username = username,
                            password = password)
        if user is not None:
            login(request, user)
            return redirect ('income_list')
        return render (request, 'auth/login.html', {'username':username,
                                                    'error': 'Incorrect data'})
    
def logout_view(request):
    try:
        logout(request)
        return redirect ('login')
    except Exception as ex:
        return HttpResponse(str(ex))
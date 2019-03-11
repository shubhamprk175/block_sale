from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
'''
def user(request, user_id):
    return render(request, 'user.html', name="user")
'''
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            print("You are now registered")
            return redirect("index")
        else:
            return render(request, "pages/register.html",
                            context={"form":form})
        print(username)
    print("You are not registered")
    form = RegisterForm()
    return render(request,
                    "pages/register.html",
                    context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                print("You are now logged in")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
            print("Invalid username or password")

    form = AuthenticationForm()
    return render(request,
                    "pages/login.html",
                    {"form":form})

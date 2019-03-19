from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from .forms import RegisterForm
from users.models import User

# Create your views here.
'''
def user(request, user_id):
    return render(request, 'user.html', name="user")
'''
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['c_password']
        balance = request.POST['balance']
        image = request.POST['image']

        # Check Passwords
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
                return redirect('register')
            else:
                # Check Email
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already being used")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password,
                    first_name=first_name, last_name=last_name, balance=balance, image=image)
                    user.save()
                    messages.success(request, "You're successfully registered and can log in")
                    print("You are not registered")
                    return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    else:
        return render(request, 'pages/register.html')

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

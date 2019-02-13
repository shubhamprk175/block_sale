from django.shortcuts import render

# Create your views here.
def user(request, user_id):
    return render(request, 'user.html', name="user")

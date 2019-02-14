from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('<int:user_id>', views.user, name='user'),
    path("register/", views.register, name = "register"),
    path("logout/", views.logout_request, name = "logout"),
	path("login/", views.login_request, name="login")
]

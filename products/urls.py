from django.contrib import admin
from django.urls import path, include


from . import views


urlpatterns = [
    path('', views.products, name='products'),
    path('<int:product_id>', views.products, name='product'),
]

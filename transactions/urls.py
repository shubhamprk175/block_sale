from django.contrib import admin
from django.urls import path, include


from . import views


urlpatterns = [
    path('<int:product_id>', views.confirm, name='confirm_tr'),
    path('', views.completed, name='completed_tr'),

]

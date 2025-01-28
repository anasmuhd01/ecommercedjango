from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('edit/<pk>', views.edit, name='edit'),
    path('delete/<pk>', views.delete, name='delete'),
    path('list/<pk>', views.list, name='list'),
    path('', views.list, name='list'),
    
]

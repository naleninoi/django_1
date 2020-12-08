from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from basketapp import views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket, name='view'),
    path('add/<int:pk>/', basketapp.add, name='add'),
    path('delete/<int:pk>/', basketapp.delete, name='delete'),
]

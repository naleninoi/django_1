from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from basketapp import views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket, name='view'),
    path('add/<int:pk>/', basketapp.basket_add, name='add'),
    path('remove/<int:pk>/', basketapp.basket_remove, name='remove'),
    path('remove/ajax/<int:pk>/', basketapp.basket_remove_ajax, name='remove_ajax'),
    path('edit/<int:pk>/<int:quantity>/', basketapp.basket_edit, name='edit'),
]

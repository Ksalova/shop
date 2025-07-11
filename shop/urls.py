from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', catalog, name='catalog'),
    path('order_create/', order_create, name='order_create'),
    path('orders/', orders, name='orders'),
]
from django.contrib import admin
from django.urls import path, include
import orders.views

urlpatterns = [
    path('', orders.views.index),
    path('create/<product_id>', orders.views.create_order, name="create_order_route"),
]

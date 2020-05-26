from django.contrib import admin
from django.urls import path, include
import profiles.views

urlpatterns = [
    path('', profiles.views.index, name='show_profile_route'),
    path('orders/', profiles.views.view_profile_orders, name='show_profile_orders_route'),
    path('reviews/', profiles.views.index, name='show_profile_reviews_route'),
]

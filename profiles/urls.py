from django.contrib import admin
from django.urls import path, include
import profiles.views

urlpatterns = [
    path('', profiles.views.index, name='show_profile_route'),
    path('orders/', profiles.views.view_profile_orders, name='show_profile_orders_route'),
    path('reviews/', profiles.views.index, name='show_profile_reviews_route'),
    path('create/', profiles.views.create_profile, name='create_profile_route'),
    path('update/', profiles.views.update_profile, name='update_profile_route'),
    path('prompt/', profiles.views.prompt_profile, name='prompt_profile_route')
]

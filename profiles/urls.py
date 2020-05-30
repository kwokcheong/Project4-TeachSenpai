from django.contrib import admin
from django.urls import path, include
import profiles.views

urlpatterns = [
    path('', profiles.views.index, name='show_profile_route'),
    path('orders/', profiles.views.view_profile_orders, name='show_profile_orders_route'),
    path('reviews/', profiles.views.view_profile_reviews, name='show_profile_reviews_route'),
    path('balance/', profiles.views.view_profile_balance, name='show_profile_balance_route'),
    path('create/', profiles.views.create_profile, name='create_profile_route'),
    path('update/', profiles.views.update_profile, name='update_profile_route'),
    path('delete/<profile_id>', profiles.views.delete_profile, name='delete_profile_route'),
    path('prompt/', profiles.views.prompt_profile, name='prompt_profile_route'),
    path('prompt/teach/', profiles.views.prompt_teaching_profile, name='prompt_teaching_profile_route')
]

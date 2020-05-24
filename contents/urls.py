from django.contrib import admin
from django.urls import path, include
import contents.views

urlpatterns = [
    path('', contents.views.index, name="show_content_route")
]

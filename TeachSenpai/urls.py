"""TeachSenpai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import products.views
import reviews.views
import orders.views
import profiles.views
import cart.views
import contents.views
import checkout.views


urlpatterns = [
    path('', products.views.home, name="homepage"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('reviews/', include('reviews.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('cart/', include('cart.urls')),
    path('contents/', include('contents.urls')),
    path('profiles/', include('profiles.urls')),
    path('checkout/', include('checkout.urls'))
]

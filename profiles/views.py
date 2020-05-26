from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from products.models import Product
from products.forms import ProductForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from orders.models import Order

# Create your views here.

@login_required
def index(request):
    products = Product.objects.all()
    return render(request, 'profiles/index.template.html', {
        'products': products
    })

def view_profile_orders(request):
    orders = Order.objects.all()
    user = request.user
    return render(request, 'profiles/profile_orders.template.html', {
        'orders': orders,
        'user': user
    })
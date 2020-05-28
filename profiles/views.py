from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from products.models import Product
from products.forms import ProductForm
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from orders.models import Order
from .models import Profile

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

@login_required
def create_profile(request):
    if request.method == 'POST':
        create_form = ProfileForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(index))
        else:
            return render(request, 'profiles/create.template.html',{
                'form': create_form
            })
    else:
        create_form = ProfileForm()
        return render(request, 'profiles/create.template.html',{
            'form': create_form
        })


def update_profile(request): 
    #1. Get the product id
    user = request.user
    profile_being_updated = get_object_or_404(Profile, pk=user.profile.id)
    profile_form = ProfileForm(request.POST, instance = profile_being_updated)
    if request.method == "POST":
        #2. Make the form to edit
        profile_form = ProfileForm(request.POST, instance = profile_being_updated)
        
        #3. Enable edit function
        if profile_form.is_valid():
            profile_form.save()
            return redirect(reverse(index))
        
        else: 
            return render(request, 'profiles/update.template.html',{
                'form': profile_form
            })
        
    else:
        profile_form = ProfileForm(instance = profile_being_updated)
        return render(request, 'profiles/update.template.html', {
            'form': profile_form
        })


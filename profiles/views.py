from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from products.models import Product
from products.forms import ProductForm
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from orders.models import Order
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist
from products.views import home

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

def view_profile_balance(request):
    user = request.user
    orders = Order.objects.all()
    return render(request, 'profiles/profile_balance.template.html',{
        'user': user,
        'orders': orders
    })

@login_required
def create_profile(request):
    if request.method == 'POST':
        create_form = ProfileForm(request.POST)
        if create_form.is_valid():
            profile = create_form.save(commit=False)
            profile.owner = request.user
            profile.save()
            messages.success(request, "Your profile has been successfully created.")
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

@login_required
def update_profile(request): 
    #1. Get the product id
    user = request.user
    profile_being_updated = get_object_or_404(Profile, pk=user.profile.id)
    profile_form = ProfileForm(request.POST, instance = profile_being_updated)
    orders = Order.objects.all()
    if request.method == "POST":
        #2. Make the form to edit
        profile_form = ProfileForm(request.POST, instance = profile_being_updated)
        
        #3. Enable edit function
        if profile_form.is_valid():
            profile_form.save()
            return redirect(reverse(index))
        
        else: 
            return render(request, 'profiles/update.template.html',{
                'form': profile_form,
                'user': user,
                'orders': orders,
            })
        
    else:
        profile_form = ProfileForm(instance = profile_being_updated)
        return render(request, 'profiles/update.template.html', {
            'form': profile_form,
            'user': user,
            'orders': orders,
        })

def prompt_profile(request):

    try:
        user = request.user
        user.profile
    except ObjectDoesNotExist:
        return redirect(reverse(create_profile))
 
    return redirect(reverse(update_profile))
    
def prompt_teaching_profile(request):
    try:
        user = request.user
        user.profile
    except ObjectDoesNotExist:
        return redirect(reverse(create_profile))
 
    return redirect(reverse(index))

@login_required
def delete_profile(request, profile_id):
    profile_to_delete = get_object_or_404(Profile, pk=profile_id)

    if request.method == "POST":
        profile_to_delete.delete()
        messages.success(request, "Your profile has been successfully deleted.")
        return redirect(reverse(home))
    return render(request, 'profiles/delete.template.html', {
        'profile': profile_to_delete
    })
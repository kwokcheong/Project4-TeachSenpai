from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.template.html', {
        'products': products
    })

@login_required
def create_product(request):
    if request.method == 'POST': 
            create_form = ProductForm(request.POST)
            if create_form.is_valid(): 
                create_form.save() 
                messages.success(request, "New product has been created")
                return redirect(reverse(index))
            else:
                return render(request, 'books/create.template.html', {
                    'form': create_form
                })
    else:
        create_form = ProductForm()
        return render(request, 'products/create.template.html',{
            'form': create_form
        })


def update_product(request, product_id): 
    #1. Get the product id
    product_being_updated = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        #2. Make the form to edit
        product_form = ProductForm(request.POST, instance = product_being_updated)
        
        #3. Enable edit function
        if product_form.is_valid():
            product_form.save()
            return redirect(reverse(index))
        
        else: 
            return render(request, 'products/update.template.html',{
                'form': product_form
            })
        
    else:
        product_form = ProductForm(instance = product_being_updated)
        return render(request, 'products/update.template.html', {
            'form': product_form
        })

def delete_product(request, product_id):
    product_to_delete = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        product_to_delete.delete()
        return redirect(reverse(index))
    return render(request, 'products/delete.template.html', {
        'product': product_to_delete
    })
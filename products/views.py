from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Product, Category
from .forms import ProductForm, SearchForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from orders.forms import OrderForm
from django.db.models import Q

# Create your views here.

def home(request):
    products = Product.objects.all()
    search_form = SearchForm(request.GET)
    category = Category.objects.all()
        # if there is any search queries submitted
    if request.GET:
        # always true query:
        queries = ~Q(pk__in=[])

        # if a title is specified, add it to the query
        if 'title' in request.GET and request.GET['title']:
            title = request.GET['title']
            queries = queries & Q(title__icontains=title)

        # if a genre is specified, add it to the query
        if 'category' in request.GET and request.GET['category']:
            category = request.GET['category']
            queries = queries & Q(category__in=category)

        # update the existing book found
        products = products.filter(queries)
        return render(request, 'products/index.template.html', {
            'products': products,
            'search_form': search_form,
            'category': category
        })
    else:
        return render(request, 'products/home.template.html', {
            'products': products
        })

def index(request):
    products = Product.objects.all()
    search_form = SearchForm(request.GET)
    category = Category.objects.all()
        # if there is any search queries submitted
    if request.GET:
        # always true query:
        queries = ~Q(pk__in=[])

        # if a title is specified, add it to the query
        if 'title' in request.GET and request.GET['title']:
            title = request.GET['title']
            queries = queries & Q(title__icontains=title)

        # if a genre is specified, add it to the query
        if 'category' in request.GET and request.GET['category']:
            category = request.GET['category']
            queries = queries & Q(category__in=category)

        # update the existing book found
        products = products.filter(queries)
    return render(request, 'products/index.template.html', {
        'products': products,
        'search_form': search_form,
        'category': category
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
                return render(request, 'products/create.template.html', {
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


def view_product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order_form = OrderForm()
    return render(request, 'products/details.template.html', {
        'product': product,
        'form': order_form
    })
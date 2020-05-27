from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from products.models import Product
from products.views import index
from orders.models import Order
from orders.forms import OrderForm

SHOPPING_CART = "shopping_cart"

# Create your views here.

def view_cart(request):
    # retrieve the cart
    cart = request.session.get('shopping_cart', {})
    
    return render(request, 'cart/view_cart.template.html', {
        'cart':cart
    })

def add_to_cart(request, product_id, title, content):

    cart = request.session.get(SHOPPING_CART, {})

    product = get_object_or_404(Product, pk=product_id)

    obtain_order = Order.objects.filter(product=product)

    # CASE ONE: The product that the user is adding is not in the shopping cart yet
    if product_id not in cart:

        cart[product_id] = {
            'id': product_id,
            'title': product.title,
            'cost': float(product.price),
            'qty': 1,
            'order_title': request.POST.get('title', False),
            'order_content': request.POST.get('content', False)
        }
        messages.success(request, f"product: {product.title} has been added to your cart")
    # CASE TWO: the product that the user is adding is ALREADY in the shopping cart
    else:
        cart[product_id]['qty'] += 1
        messages.success(request, f"One more product: {product.title} has been added to your cart")

    #  save back to the session
    request.session[SHOPPING_CART] = cart

    return redirect(reverse('show_product_route'))


def remove_from_cart(request, product_id):
    # retrieve the cart from session
    cart = request.session.get('shopping_cart',{})
    
    # if the product is in the cart
    if product_id in cart:
        # remove it from the cart
        del cart[product_id]
        # save back to the session
        request.session['shopping_cart'] = cart
        messages.success(request, "Item removed from cart successfully!")
        
    return redirect(reverse('show_product_route'))

def update_quantity(request, product_id):
    cart = request.session.get('shopping_cart')
    if product_id in cart:
        cart[product_id]['qty'] = request.POST['qty']
        request.session['shopping_cart'] = cart
        messages.success(request, f"Quantity for {cart[product_id]['title']} has been changed")

    return redirect(reverse('view_cart_route'))
from django.shortcuts import render, reverse, HttpResponse, get_object_or_404

#import settings so that we can access the public stripe key
from django.conf import settings
import stripe
from products.models import Product
from orders.models import Order
from django.contrib.sites.models import Site

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    # retrieve shopping cart
    cart = request.session.get('shopping_cart', {})
    
    line_items = []
    
    # Explanation A: generate the line_items
    for id, order in cart.items():
        # For each item in the cart, get its details from the database
        product_object = get_object_or_404(Product, pk=id)
        
        line_items.append({
            'name': product_object.title,
            'amount': int(product_object.price*100), #convert to cents, in integer
            'currency':'sgd',
            'quantity': 1
        })

    current_site = Site.objects.get_current()
    domain = current_site.domain


    # Explanation B: generate the session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        success_url=domain + reverse(checkout_success),
        cancel_url=domain + reverse(checkout_cancelled),
    )
    
    # render the template
    return render(request, 'checkout/checkout.template.html', {
        'session_id':session.id,
        'public_key': settings.STRIPE_PUBLISHABLE_KEY
    })
    
def checkout_success(request):
    
    cart = request.session.get('shopping_cart', {})
    record_order = "no_item"
    for id, order in cart.items():
      product_object = get_object_or_404(Product, pk=id)

      record_order = Order.objects.create(
          title=order['order_title'],
          product=product_object,
          owner=request.user,
          content=order['order_content'],
          resolve= "unresolved"
      )

    request.session['shopping_cart'] = {}
    return render(request, 'checkout/checkout_success.template.html',{
        'orders': record_order
    })
    
def checkout_cancelled(request):
    return HttpResponse("Checkout cancelled")



@csrf_exempt
def payment_completed(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.SIGNING_SECRET
        )
    except ValueError as e:
        # Invalid payload
        print(e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print(e)
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

    # Fulfill the purchase...
    handle_checkout_session(session)



    return HttpResponse(status=200)


def handle_checkout_session(session):
    print(session)
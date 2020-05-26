from django.shortcuts import render, reverse, HttpResponse, get_object_or_404

#import settings so that we can access the public stripe key
from django.conf import settings
import stripe
from products.models import Product
from django.contrib.sites.models import Site

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def checkout(request, product_id):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    # retrieve product
    product = request.get('shopping_cart')
    
    line_items = []

    # For each item in the cart, get its details from the database
    product_object = get_object_or_404(product, pk=product.id)
    line_items.append({
        'name': product_object.title,
        'amount': int(product_object.price*100), #convert to cents, in integer
        'currency':'sgd'
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
    return HttpResponse("Checkout success")
    
def checkout_cancelled(request):
    return HttpResponse("Checkout cancelled")

@csrf_exempt
def payment_completed(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, endpoint_secret
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

  # Handle the checkout.session.completed event
  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']

    # Fulfill the purchase...
    handle_checkout_session(session)

  return HttpResponse(status=200)
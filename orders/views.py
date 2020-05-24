from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Order, Product
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import OrderForm

# Create your views here.
def index(request):
    orders = Order.objects.all()
    user = request.user
    return render(request, 'orders/index.template.html', {
        'orders': orders,
        'user': user
    })

def create_order(request, product_id):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
        # create an instance of order, but don't commit, so that we have a chance to set the user
            order = form.save(commit=False)
            order.owner = request.user
            order.product = get_object_or_404(Product, pk=product_id)
            order.save()
            messages.success(request, "New order has been added - " + order.title)
            return redirect(reverse(index))
        else:
            return render(request, 'orders/create_order.template.html', {
                'form': form
            })
    else:
        form = OrderForm()
        return render(request, 'orders/create_order.template.html', {
            'form': form
        })
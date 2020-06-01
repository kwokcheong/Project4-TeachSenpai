from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from orders.models import Order
from products.models import Product
from products.views import home


# Create your views here.
def index(request):
    review = Review.objects.all()
    return render(request, 'reviews/index.template.html',{
        'review': Review
    })

@login_required
def create_review(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.owner = request.user
            order = get_object_or_404(Order, pk=order_id)
            review.order = order
            review.product = get_object_or_404(Product, pk=order.product.id)
            review.save()
            messages.success(request, "Thank you for the review.")
            return redirect(reverse(home))
    else:
        create_form = ReviewForm()
        return render(request, 'reviews/create.template.html',{
            'order': order,
            'form': create_form
        })
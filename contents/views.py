from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Material
from django.contrib.auth.decorators import login_required, permission_required
from .models import Order, Product
from django.contrib import messages
from .forms import MaterialForm

# Create your views here.
def index(request):
    materials = Material.objects.all()
    user = request.user
    return render(request, 'contents/index.template.html', {
        'materials': materials,
        'user': user
    })


def create_material(request, order_id): 
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save(commit=False)
            material.owner = request.user
            material.order = get_object_or_404(Order, pk=order_id)
            material.save()
            return redirect(reverse(index))
        else:
            return render(request, 'contents/create_content.template.html', {
                'form': form
            })
    else:
        form = MaterialForm()
        return render(request, 'contents/create_content.template.html', {
            'form': form
        })
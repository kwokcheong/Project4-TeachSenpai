from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Material
from django.contrib.auth.decorators import login_required, permission_required
from .models import Order, Product
from django.contrib import messages
from .forms import MaterialForm
from orders.forms import ResolveForm

# Create your views here.
def index(request):
    materials = Material.objects.all()
    user = request.user
    return render(request, 'contents/index.template.html', {
        'materials': materials,
        'user': user
    })

def show_material(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    materials = Material.objects.all()
    form = ResolveForm(initial={'resolve': "resolved"})

    if request.method == "POST":
        form = ResolveForm(request.POST, instance=order)
        form.save()
    

    return render(request, 'contents/show_material.template.html', {
        'materials': materials,
        'order_id': int(order_id),
        'form': form
    })


@login_required
def create_material(request, order_id, product_id): 
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save(commit=False)
            material.owner = request.user
            material.order = get_object_or_404(Order, pk=order_id)
            material.product = get_object_or_404(Product, pk=product_id)
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

def update_material(request, order_id):
    material_being_updated = get_object_or_404(Material, pk=order_id)

    if request.method == "POST":
        #2. Make the form to edit
        material_form = MaterialForm(request.POST, instance = material_being_updated)
        
        #3. Enable edit function
        if material_form.is_valid():
            material_form.save()
            return redirect(reverse(index))
        
        else: 
            return render(request, 'contents/update.template.html',{
                'form': material_form,
                'order_id': order_id
            })
        
    else:
        material_form = MaterialForm(instance = material_being_updated)
        return render(request, 'contents/update.template.html', {
            'form': material_form,
            'order_id': order_id
        })
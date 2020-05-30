from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Material
from django.contrib.auth.decorators import login_required, permission_required
from .models import Order, Product
from profiles.models import Profile
from django.contrib import messages
from .forms import MaterialForm, CommentForm
from orders.forms import ResolveForm
from django.db.models import F, Count

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
    user = request.user
    if request.method == "POST":
        product_id = order.product.id
        product = get_object_or_404(Product, pk=product_id)
        user = product.owner
        Profile.objects.filter(pk=user.profile.id).update(balance= (F('balance') + int(product.price)) )
        form = ResolveForm(request.POST, instance=order)
        form.save()
    

    return render(request, 'contents/show_material.template.html', {
        'materials': materials,
        'order_id': int(order_id),
        'order': order,
        'form': form,
        'user': user
    })

def comment_room(request, material_id):
    material = get_object_or_404(Material,pk=material_id )
    user = request.user
    comments = material.comments.order_by("-created_on")
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.name = user.username
            new_comment.material = material
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    return render(request, 'contents/comment_room.template.html',{
        'form': comment_form,
        'comments': comments,
        'material': material
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
            return redirect(reverse(show_material, args=(order_id,)))
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

def delete_material(request, material_id):
    material_to_delete = get_object_or_404(Material, pk=material_id)

    if request.method == "POST":
        material_to_delete.delete()
        orders = Order.objects.all()
        user = request.user
        return render(request, 'profiles/profile_orders.template.html', {
            'orders': orders,
            'user': user
        })
    return render(request, 'contents/delete.template.html',{
        'material': material_to_delete
    })
    
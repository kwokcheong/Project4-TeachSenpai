from django.contrib import admin
from django.urls import path, include
import products.views

urlpatterns = [
    path('', products.views.index, name='show_product_route'),
    path('create', products.views.create_product, name="create_product_route"),
    path('update/<product_id>', products.views.update_product, name='update_product_route'),
    path('delete/<product_id>', products.views.delete_product, name='delete_product_route')
]

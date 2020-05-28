from django.contrib import admin
from django.urls import path, include
import contents.views

urlpatterns = [
    path('create/<product_id>/<order_id>', contents.views.create_material, name="create_content_route"),
    path('update/<order_id>', contents.views.update_material, name='update_content_route'),
    path('show/<order_id>', contents.views.show_material, name='show_content_route'),
    path('delete/<material_id>', contents.views.delete_material, name='delete_content_route')
]

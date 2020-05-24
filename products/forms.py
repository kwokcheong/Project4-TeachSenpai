from django import forms
from .models import Product, Category, Tag
from pyuploadcare.dj.forms import ImageField


class ProductForm(forms.ModelForm):
    image = ImageField(label='', required=False)
    class Meta:
        model = Product
        fields = ('title', 'image', 'desc', 'price', 'category', 'tag', 'owner', 'video')
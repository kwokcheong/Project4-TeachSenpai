from django import forms
from .models import Product, Category, Tag
from pyuploadcare.dj.forms import ImageField


class ProductForm(forms.ModelForm):
    image = ImageField(label='', required=False)
    class Meta:
        model = Product
        fields = ('title', 'image', 'desc', 'price', 'category', 'tag', 'owner', 'video')


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)

class CategoryForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
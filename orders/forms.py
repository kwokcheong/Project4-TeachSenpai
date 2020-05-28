from django import forms
from .models import Order

class ResolveForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('resolve',)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('title', 'content')
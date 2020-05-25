from django import forms
from .models import Material
from pyuploadcare.dj.forms import ImageField


class MaterialForm(forms.ModelForm):
    image = ImageField(label='', required=False)
    class Meta:
        model = Material
        fields = ('content', 'video', 'image')
from django import forms
from .models import Material, Comment
from pyuploadcare.dj.forms import ImageField


class MaterialForm(forms.ModelForm):
    image = ImageField(label='', required=False)
    class Meta:
        model = Material
        fields = ('content', 'video', 'image')

class CommentForm(forms.ModelForm):
    image = ImageField(label='', required=False)
    class Meta:
        model = Comment
        fields = ('body','image',)
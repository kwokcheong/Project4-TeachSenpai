from django import forms
from pyuploadcare.dj.forms import ImageField
from .models import Profile


class ProfileForm(forms.ModelForm):
    image = ImageField(label='', required=False)
    class Meta:
        model = Profile
        fields = ('username', 'email', 'owner', 'profiledesc', 'profileimg')
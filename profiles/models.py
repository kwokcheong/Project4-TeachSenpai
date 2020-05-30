from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
# Create your models here.

class Profile(models.Model): 
    username = models.CharField(blank=False, max_length=255)
    email = models.CharField(max_length=200, null=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profiledesc = models.TextField(blank=False)
    profileimg = ImageField(blank=True, manual_crop="")
    balance = models.DecimalField(max_digits= 9, decimal_places=2, default=0)

    def __str__(self):
        return self.username


from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from django.utils.timezone import now
from products.models import Product
from orders.models import Order

# Create your models here.
class Material(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    posted_when = models.DateTimeField(blank=False, auto_now=True)
    content = models.TextField(blank=False)
    video = models.URLField(blank=True, max_length = 200)
    image = ImageField(blank=True, manual_crop="")
  

    def __str__(self):
        return "RE: " + self.order.title
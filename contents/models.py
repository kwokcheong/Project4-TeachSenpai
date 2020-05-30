from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from django.utils.timezone import now
from products.models import Product
from orders.models import Order
from pyuploadcare.dj.models import ImageField

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


class Comment(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = ImageField(blank=True, manual_crop="")

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
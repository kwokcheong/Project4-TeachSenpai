from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from products.models import Product
from orders.models import Order
# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    posted_when = models.DateTimeField(blank=False, auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 
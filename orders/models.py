from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from products.models import Product
import uuid

# Create your models here.

class Order(models.Model):
    title = models.CharField(blank=False, max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_when = models.DateTimeField(blank=False, auto_now=True)
    content = models.TextField(blank=False)
    resolve = models.CharField(blank=False, max_length=30)
    secret_id = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title + " for: " + self.product.title
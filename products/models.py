from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    title = models.CharField(blank=False, max_length=255)
    def __str__(self):
        return self.title 

class Category(models.Model):
    title = models.CharField(blank=False, max_length=255)
    def __str__(self):
        return self.title

class Product(models.Model): 
    title = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    price = models.DecimalField(max_digits =5, decimal_places =2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    video = models.URLField(blank=True, max_length = 200)

    def __str__(self):
        return self.title


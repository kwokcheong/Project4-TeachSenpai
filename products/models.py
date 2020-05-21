from django.db import models

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

    def __str__(self):
        return self.title


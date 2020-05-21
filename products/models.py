from django.db import models

# Create your models here.
class Product(models.Model): 
    title = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    price = models.DecimalField(max_digits =5, decimal_places =2)

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='product', default='no-img.jpeg')
    
    def __str__(self):
        return self.name

class Merch(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='merch', default='no-img.jpeg')

    def __str__(self):
        return self.name
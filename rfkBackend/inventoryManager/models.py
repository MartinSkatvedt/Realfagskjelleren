from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='product', default='no-img.jpeg')
    active = models.BooleanField(default=True)
    
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


class ProductCount(models.Model):
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name + " " + str(self.amount)

class TotalProductCount(models.Model):
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None)
    data = models.ManyToManyField(ProductCount)

    def __str__(self):
        return self.author.username + " " + str(self.date)
from django.db import models

# Create your models here.
class PrivateFile(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='private', default='no-img.jpeg')
    
    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
class BlogMessage(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    text = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
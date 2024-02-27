from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField()
    bgimage=models.ImageField(upload_to='pics',blank=True)
    
    def __str__(self):
        return '{}'.format(self.name)
    
    def get_url(self):
        return reverse('services:by_category',args=[self.slug])

class Types(models.Model):
    name = models.CharField(max_length=255)
    mobile=models.IntegerField(max_length=10)
    date=models.DateField(auto_now_add=True)
    slug=models.SlugField(max_length=250,unique=True)

    def __str__(self):
        return '{}'.format(self.name)
    

    
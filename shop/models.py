from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse




Product_cartegories =(
    ("L", "Laptops"),
    ("P", "Phones"),
    ("M", "Microphones"),
    ("S", "Speakers"),
)
  
class product(models.Model):
     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
     name = models.CharField(max_length=200, null=True, blank=True)
     brand = models.CharField(max_length=200, null=True, blank=True)
     cartegory = models.CharField(choices=Product_cartegories, max_length=1)
     image = models.ImageField(null=True, blank=True)
     description = models.TextField(null=True, blank=True)
     price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
     date = models.DateTimeField(auto_now_add=True)
     slug = models.SlugField(max_length=200, null=True, blank=True)

     class Meta:
        ordering = ['-date']


     def __str__(self):
        return self.name

     


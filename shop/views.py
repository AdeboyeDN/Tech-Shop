from django.shortcuts import render
from .models import product
from django.views.generic import ListView



class ProductHomeList(ListView):
    model = product
    context_object_name = 'products'
    template_name= 'shop/home.html'
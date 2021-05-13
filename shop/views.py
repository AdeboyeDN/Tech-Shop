from django.shortcuts import render
from .models import product
from django.views.generic import ListView, DetailView



class ProductHomeList(ListView):
    model = product
    context_object_name = 'products'
    template_name= 'shop/home.html'


class ProductDetail(DetailView):
    model = product
    context_object_name = "product"
    template_name='shop/details.html'
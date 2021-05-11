from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
     path('',  views.ProductHomeList.as_view(), name='home-page'),
     path('cart/',  TemplateView.as_view(template_name="shop/cart.html"), name='cart-page'),
     path('profile/',  TemplateView.as_view(template_name="shop/profile.html"), name='profile-page'),

]

from django.shortcuts import render
from cart. models import *
# Create your views here.

def checkout(request):
    cart_items = CartItems.objects.filter()
    context = {
        'cartit':cart_items
    }
    return render(request,'core/checkout.html',context)
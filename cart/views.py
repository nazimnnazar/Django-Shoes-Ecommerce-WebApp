from django.shortcuts import render,redirect
from core.models import*
from . models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

@login_required(login_url='login')
def cart(request,tot=0,count=0,cart_items=None):
    try:
        cart = CartList.objects.get(cart_id=c_id(request))
        cart_items = CartItems.objects.filter(cart=cart)
        for i in cart_items:
            tot +=(i.product.price * i.quantity)
            count += i.quantity
    except ObjectDoesNotExist:
        pass
    context = {
        'cartitem':cart_items,
        'total':tot,
        'count':count
    }
    return render(request,'core/cart.html',context)
@login_required(login_url='login')
def c_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id
    
@login_required(login_url='login')
def addcart(request,product_id):
    product = Products.objects.get(id=product_id)
    try:
        cart = CartList.objects.get(cart_id = c_id(request))
    except CartList.DoesNotExist:
        cart = CartList.objects.create(cart_id=c_id(request))
        cart.save()
    try:
        cart_items = CartItems.objects.get(product=product,cart=cart)
        if cart_items.quantity < cart_items.product.stock:
            cart_items.quantity += 1
        cart_items.save()
    except CartItems.DoesNotExist:
        cart_items = CartItems.objects.create(product=product,quantity=1,cart=cart)
        cart_items.save()
    messages.success(request,("Product SuccessFulyy Added!!!"))
    return redirect('cart')

@login_required(login_url='login')
def dicrement(request, product_id):
    cart = CartList.objects.get(cart_id=c_id(request))
    product = get_object_or_404(Products,id=product_id)
    cart_items = CartItems.objects.get(product=product,cart=cart)
    if cart_items.quantity >1:
        cart_items.quantity -=1
        cart_items.save()
    else:
        cart_items.delete()
    messages.success(request,("Oopss your product quantity dicremented!!!"))
    return redirect('cart')

@login_required(login_url='login')
def delete(request, product_id):
    cart = CartList.objects.get(cart_id=c_id(request))
    product = get_object_or_404(Products,id=product_id)
    cart_items = CartItems.objects.get(product=product,cart=cart)
    cart_items.delete()
    messages.success(request,("Product SuccessFulyy removed!!!"))
    return redirect('cart')
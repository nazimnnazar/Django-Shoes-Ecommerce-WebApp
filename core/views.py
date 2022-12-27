from django.shortcuts import render
from . models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
def frontpage(request):
    product = Products.objects.all()[0:8]
    context = {
        'product':product
    }
    return render(request,'core/index.html',context)

@login_required(login_url='login')
def mens(request):
    product = Products.objects.all()
    categ = Category.objects.all()
    paginator = Paginator(Products.objects.all(),12)
    page = request.GET.get('page')
    paginat = paginator.get_page(page)
    context = {
        'product':product,
        'paginat':paginat,
        'categ':categ,
    }
    return render(request,'core/men.html',context)
    
@login_required(login_url='login')
def product_view(request,pk):
    prod = Products.objects.all()[16:20]
    categ = Category.objects.all()
    product = Products.objects.get(id=pk)
    context = {
        'product':product,
        'products':prod,
        'categ':categ,
    }
    return render(request,'core/product_view.html',context)

@login_required(login_url='login')
def about(request):
    return render(request,'core/about.html')


# def contact(request):
    # if request.method == 'POST':
    #     message_name =request.POST['message-name']
    #     message_email = request.POST['message-email']
    #     message = request.POST['message']
    #     context={
    #         'message':message_name
    #     }
    #     return render(request,'core/contact.html',context)
    # else:
    #     return render(request,'core/contact.html')
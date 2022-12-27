from django.shortcuts import render
from core.models import *
from django.db.models import Q
# Create your views here.
def search(request):
    product=None
    query=None
    if 'search' in request.GET:
        query = request.GET.get('search')
        product = Products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    
    return render(request,'core/search.html',{
    'query':query,
    'product':product})
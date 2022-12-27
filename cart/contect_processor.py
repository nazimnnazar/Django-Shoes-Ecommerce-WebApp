from . models import *
from . views import *

def count(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = CartList.objects.filter(cart_id=c_id(request))
            cart_item = CartItems.objects.filter(cart=cart[:1])
            for i in cart_item:
                item_count +=i.quantity
        except CartList.DoesNotExist:
            item_count=0
        return dict(itc=item_count)
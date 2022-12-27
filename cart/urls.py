from django.urls import path
from . import views

urlpatterns = [
    path('cart/',views.cart,name='cart'),
    path('add/<int:product_id>/',views.addcart,name='addcart'),
    path('dicrement/<int:product_id>/',views.dicrement,name='dicrement'),
    path('delete/<int:product_id>',views.delete,name='delete'),
]
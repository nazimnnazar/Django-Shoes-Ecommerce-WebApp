from django.urls import path
from . import views

urlpatterns = [
    path('',views.frontpage,name='frontpage'),
    path('mens/',views.mens,name='mens'),
    path('product/<str:pk>/',views.product_view,name='product'),
    path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
]
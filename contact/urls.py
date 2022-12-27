from django.urls import path
from . import  views 
urlpatterns = [
    path('contact/',views.contact,name='contact'),
    path('contactdone/',views.contactdone,name='contactdone'),
]

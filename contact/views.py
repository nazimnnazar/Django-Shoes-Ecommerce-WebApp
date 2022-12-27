from django.shortcuts import render,redirect
from . models import*
from django.contrib import messages
def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        messages.success(request,("Your Message SuccessFulyy Got It!!!"))
        return redirect('contactdone')
    return render(request,'core/contact.html')

def contactdone(request):
    return render(request,'core/contactdone.html')
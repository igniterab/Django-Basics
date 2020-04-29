from django.shortcuts import render
from home.models import contact
from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .form import *
# Create your views


'''def cont(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        content = request.POST["content"]
        mimg =  request.POST["mimg"]
        ct = contact(name=name,email=email,phone=phone,content=content,mimg=mimg)
        ct.save()
    return render(request,"home/contact.html")'''

def bot(request):
    return render(request,"home/about.html")


def home(request):

    d = contact.objects.all()
    dicti = {'dests':d}
    print(d)
    return render(request,"home/home.html",dicti)

def cont(request): 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = HotelForm() 
    return render(request, 'home/contact.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfully uploaded') 
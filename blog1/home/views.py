from django.shortcuts import render
from home.models import contact

# Create your views

def home(request):
    return render(request,"home/home.html")

def cont(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        content = request.POST["content"]
        mimg =  request.POST["mimg"]
        ct = contact(name=name,email=email,phone=phone,content=content,mimg=mimg)
        ct.save()
    return render(request,"home/contact.html")

def data(request):

    d = contact.objects.all()
    dicti = {'dests':d}
    print(d)
    return render(request,"home/about.html",dicti)
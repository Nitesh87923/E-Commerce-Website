from django.shortcuts import render
from e_commerce_app.models import Contact,Product
from django.contrib import messages
from math import ceil
# Create your views here.
def index(request):

    allProds = []
    catprods = Product.objects.values('category','id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params= {'allProds':allProds}

    return render(request,"index.html",params)


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        desc=request.POST['desc']
        ph=request.POST['pnumber']
        myquery=Contact(name=name,email=email,ph=ph,desc=desc)
        myquery.save()
        messages.info(request,"Thank You! We will get back to you at the earliest.")
        return render(request,'contact.html')
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")
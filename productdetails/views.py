from django.shortcuts import render
from django.http import HttpResponse
from productdetails.models import product

# Create your views here.
def addproduct(request):
    if request.method=='POST':
        product.objects.create(
            productName=request.POST.get('prodname'),
            productPrice=request.POST.get('prodprice'),
        )
        return HttpResponse('Your record saved successfuly!')
        
    return render(request,'index.html')

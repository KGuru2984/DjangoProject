from django.shortcuts import render
from customers.custmodule import custdetails
from django.http import HttpResponse

# Create your views here.
def customerview(request):
    if request.method=='POST':
        cnm=request.POST.get('customername')
        cadd=request.POST.get('customeraddress')
        message=custdetails.addcustomerrec(cnm,cadd)
        return HttpResponse(message)
        
    return render(request,'customerview.html')

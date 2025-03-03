from django.shortcuts import render,redirect
from productcatalog.productmodule import ProductCatalogClass
from django.utils import timezone
from UserWelcomePage.UserWelcomeModel import UserWelcomeData
from django.contrib import messages

# Create your views here.
def BasketView(request):
    if request.method=="POST":
        basketids=request.POST.getlist("basid")
        quantitys=request.POST.getlist("pqty",0)
        subtotal=request.POST.get("subtotal")
        request.session["tamount"]=int(float(subtotal)*100)
        print(subtotal)
        print(basketids)
        print(quantitys)
        for basketid,quantity in zip(basketids,quantitys):
            ProductCatalogClass.modifybasketquantity(basketid,quantity)
        #messages.success(request,"Record Saved Successfully!")
        return redirect('razorpayhome')
    vusername=request.session.get("username")
    vdate=timezone.now().strftime("%A, %d %B %Y")
    menulist=UserWelcomeData.getMenuOptions()
    vloginid=request.session.get("userloginid")
    basketcounter=ProductCatalogClass.getbasketviewcount(vloginid)
    basketdata=ProductCatalogClass.getbasketrec(vloginid)
    context={
        'candidatename':vusername,
        'displaydate':vdate,
        'menudata':menulist,
        'bcnt':basketcounter,
        'bdata':basketdata,
    }
    
    return render(request,'basketview.html',context)

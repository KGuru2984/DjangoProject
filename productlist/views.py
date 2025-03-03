from django.shortcuts import render
from productcatalog.productmodule import ProductCatalogClass
from django.utils import timezone
from UserWelcomePage.UserWelcomeModel import UserWelcomeData
from django.contrib import messages
# Create your views here.

def productlistview(request):
    if request.method=="POST":
        vid=request.POST.get("xid")
        resultMsg=ProductCatalogClass.removalbyproductid(vid)
        messages.success(request,resultMsg)
    allproducts=ProductCatalogClass.getAllProduct()
    vusername=request.session.get("username")
    vdate=timezone.now().strftime("%A, %d %B %Y")
    menulist=UserWelcomeData.getMenuOptions()
    vloginid=request.session.get("userloginid")
    basketcounter=ProductCatalogClass.getbasketviewcount(vloginid)
    context={
        'candidatename':vusername,
        'displaydate':vdate,
        'menudata':menulist,
        'prods':allproducts,
        'bcnt':basketcounter,
    }
    
    return render(request,"productlist.html",context)
from django.shortcuts import render
from productcatalog.productmodule import ProductCatalogClass
from django.utils import timezone
from UserWelcomePage.UserWelcomeModel import UserWelcomeData
from django.contrib import messages

# Create your views here.

def productcatalogview(request):
    vusername=request.session.get("username")
    vdate=timezone.now().strftime("%A, %d %B %Y")
    menulist=UserWelcomeData.getMenuOptions()
    productcategories=ProductCatalogClass.getProductCategories()
    vloginid=request.session.get("userloginid")
    basketcounter=ProductCatalogClass.getbasketviewcount(vloginid)
    context={
        'candidatename':vusername,
        'displaydate':vdate,
        'menudata':menulist,
        'prodcat':productcategories,
        'bcnt':basketcounter,
    }
    
    if request.method=="POST":
        vpcat=request.POST.get("catp")
        vpname=request.POST.get("pname")
        vpdesc=request.POST.get("pdesc")
        vpprice=request.POST.get("pprice")
        vpimage=request.POST.get("pimage")
        msg=ProductCatalogClass.addProductRecord(vpcat,vpname,vpdesc,vpprice,vpimage)
        splitmsg=msg.split(":")
        
        if splitmsg[0]=="Error":
            messages.error(request,splitmsg[1])
        else:
            messages.success(request,splitmsg[1])
    
    return render(request,"productcatalog.html",context)
    
    

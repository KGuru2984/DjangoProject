from django.shortcuts import render
from productcatalog.productmodule import ProductCatalogClass
from django.utils import timezone
from UserWelcomePage.UserWelcomeModel import UserWelcomeData
from django.contrib import messages
# Create your views here.

def productviewbyid(request,productid):    
    if request.method=="POST":
        vpid=request.POST.get("ppid")
        vpcategory=request.POST.get("catp")
        vpname=request.POST.get("pname")
        vpdesc=request.POST.get("pdesc")
        vpimg=request.POST.get("pimage")
        vpprice=request.POST.get("pprice")
        vpflag=request.POST.get("s1")
        
        resultMsg=ProductCatalogClass.changeproductbyid(productid,vpcategory,vpname,vpdesc,vpimg,vpprice,vpflag)
        print(resultMsg)
        messages.success(request,resultMsg)
        
    vusername=request.session.get("username")
    vdate=timezone.now().strftime("%A, %d %B %Y")
    menulist=UserWelcomeData.getMenuOptions()
    product=ProductCatalogClass.getproductbyproductid(productid)
    productcategories=ProductCatalogClass.getProductCategories()
    vloginid=request.session.get("userloginid")
    basketcounter=ProductCatalogClass.getbasketviewcount(vloginid)
    prodid, prodcaty, prodname, proddesc, prodprice, prodimg, prodflag = product[0]
    context={
        'candidatename':vusername,
        'displaydate':vdate,
        'menudata':menulist,
        'prodcat': productcategories,
        'prodid':prodid,
        'prodcaty':prodcaty, 
        'prodname':prodname,
        'proddesc':proddesc,
        'prodprice':prodprice,
        'prodimg':prodimg,
        'prodflag':prodflag,
        'bcnt':basketcounter,
    }
    
    return render(request,'productview.html',context)
    
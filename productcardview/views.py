from django.shortcuts import render
from productcatalog.productmodule import ProductCatalogClass
from django.utils import timezone
from UserWelcomePage.UserWelcomeModel import UserWelcomeData

# Create your views here.
def cardview(request):
    if request.method=="POST":
        vuid=request.session.get("userloginid")
        vpid=request.POST.get("productid")
        vpqty=request.POST.get("productqty")
        print(vpqty)
        resultMsg=ProductCatalogClass.addbasketdata(vuid,vpid,vpqty)
    
    vusername=request.session.get("username")
    vdate=timezone.now().strftime("%A, %d %B %Y")
    menulist=UserWelcomeData.getMenuOptions()
    allproducts=ProductCatalogClass.getAllProduct()
    vloginid=request.session.get("userloginid")
    basketcounter=ProductCatalogClass.getbasketviewcount(vloginid)
    context={
        'candidatename':vusername,
        'displaydate':vdate,
        'menudata':menulist,
        'prods':allproducts,
        'bcnt':basketcounter,
    }
    return render(request,'cardview.html',context)

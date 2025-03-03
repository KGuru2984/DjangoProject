from django.shortcuts import render
from django.utils import timezone
from UserWelcomePage.UserWelcomeModel import UserWelcomeData
from productcatalog.productmodule import ProductCatalogClass

# Create your views here.

def UserHomeView(request):
    vusername=request.session.get("username")
    vloginid=request.session.get("userloginid")
    basketcounter=ProductCatalogClass.getbasketviewcount(vloginid)
    vdate=timezone.now().strftime("%A, %d %B %Y")
    # %H:%M:%S
    menulist=UserWelcomeData.getMenuOptions()
    
    context={
        'candidatename':vusername,
        'displaydate':vdate,
        'menudata':menulist,
        'lid':vloginid,
        'bcnt':basketcounter,
    }
    return render(request,"UserHomePage.html",context)
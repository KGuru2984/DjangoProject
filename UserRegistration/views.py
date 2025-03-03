from django.shortcuts import render
from UserRegistration.UserModule import UserRecord
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def UserView(request):
    if request.method=="POST":
        usernm=request.POST.get("uname")
        useremail=request.POST.get("uemail")
        userpassword=request.POST.get("upassword")
        messageResult=UserRecord.addUserRecord(usernm,useremail,userpassword)
        messages.success(request,messageResult)
        #return HttpResponse(message)
    return render(request,"UserView.html")

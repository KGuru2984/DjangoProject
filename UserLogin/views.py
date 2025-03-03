from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib import sessions
from UserLogin.UserLoginModule import VerifyUser

# Create your views here.
def LoginView(request):
    userdisplayname=None
    messageType=None
    if request.method=="POST":
        usernm=request.POST.get("useremail")
        userpass=request.POST.get("userpassword")
        resultMsg=VerifyUser.ValidateLogin(usernm,userpass)
        split_message=resultMsg.split(":")
        if split_message[0]=="Error":
            messageType="Error"
            messages.error(request,split_message[1])
        else:
            messageType="Sucess"
            userdata=split_message[0].split("-")
            userdisplayname=userdata[1]
            userlid=userdata[0]
            request.session["username"]=userdisplayname
            request.session["userloginid"]=userlid
            messages.success(request,split_message[1])
            #return redirect('customerview')
       
       
    return render(request,"LoginView.html",{'userdisplayname':userdisplayname})

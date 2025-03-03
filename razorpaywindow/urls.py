from django.urls import path
from . import views

urlpatterns = [
    path('',views.razorpayhome,name="razorpayhome"),
    path('paymenthandler/',views.paymenthandler,name="paymenthandler")
]
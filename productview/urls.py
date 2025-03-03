from django.urls import path
from . import views

urlpatterns =[
    path('<int:productid>/',views.productviewbyid,name='productviewbyid')
]
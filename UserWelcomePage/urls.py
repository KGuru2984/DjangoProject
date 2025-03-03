from django.urls import path
from . import views 

urlpatterns =[
    path('',views.UserHomeView, name="UserHomeView")
]
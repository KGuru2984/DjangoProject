from django.urls import path
from . import views

urlpatterns=[
    path('',views.UserView,name="UserView")
]
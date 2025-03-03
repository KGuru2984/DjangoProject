from django.urls import path
from . import views
urlpatterns =[
    path('',views.productlistview,name="productlistview")
]
from django.urls import path
from . import views
urlpatterns =[
    path('',views.productcatalogview,name="productcatalogview")
]
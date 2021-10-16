from django.urls import path
from . import views

urlpatterns = [
    path("" , views.home , name="Home") , 
    path("about/" , views.about , name="About") , 
    path("add/" , views.add , name="Add") ,
    path("update/<int:id>" , views.update , name="Update") , 
    path("vehicle/<int:id>" , views.vehicle , name="Vehicle"),
    path("delete/<int:id>" , views.delete , name="Delete")
]
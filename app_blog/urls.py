from django.urls import path
from .import views
from app_blog.views import *

urlpatterns = [
    path('',views.myhome,name='home'),
    path('contactus/',views.ContactUs,name='contact'),
    path('addition/',views.addition,name='addition'),
    path('addition/add',views.add,name='add'),
    path('add_product/',views.add_product,name='add_product'),
    path('add_product/adddata',views.adddata,name='adddata'),
    path('add_product/<int:pk>', views.editpage ,name='editpageinfo' )
    
]
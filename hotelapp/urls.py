from os import name
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('hoteltest/',views.fnhoteltest,name='hoteltest'),


    path('base/',views.baseFn,name="base"),
    path('hoteladminhome/',views.homeFn,name="hoteladminhome"),

    path('adminsignup/',views.adminsignupFn,name="adminsignup"),
    path('adminlogin/',views.adminloginFn,name="adminlogin"),
    path('adminlogout/',views.adminlogoutFn,name="adminlogout"),

    path('bookroom/',views.fnBookRoom,name='bookroom'),
    # path('roomprice/',views.fnRoomPrice, name="roomprice"),

    path('addhotel/',views.addhotelFn, name="addhotel"),


    path('addnewhotel/',views.addnewhotelFn, name="addnewhotel"),
    path('addnewrooms/',views.addnewroomsFn, name="addnewrooms"),

]


    
    
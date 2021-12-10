from os import name
from django.urls import path
from . import views
from userapp import views

urlpatterns = [
    path('user/', views.UserFun, name='user'),
    path('home/',views.HomeFun,name='home'),
    # sign up
    path('signup/',views.fnsignup,name='signup'),
    # user login
    path('userLoginMaster/',views.fnuserLoginMaster,name='userLoginMaster'),
    path('login/',views.fnlogin,name='login'),
    path('userUpdate/',views.fnuserUpdate, name='userUpdate'),
    path('userDelete/',views.fnuserDelete, name='userDelete'),
    path('userLogout/',views.fnuserLogout, name='userlogout'),
    path('userChangePass/',views.fnchangePass, name='userChangePass'),


    path('index/',views.indexFun, name='index'),



# new
    path('masterHome/',views.masterHomeFn,name='masterHome'),
    path('contact/',views.contactFn,name='contact'),
    path('about/',views.aboutFn,name='about'),

    path('searchrooms/',views.searchroomsFn, name="searchrooms"),



    path('filterprice/',views.fnfilterprice,name="filterprice"),
    


    
]
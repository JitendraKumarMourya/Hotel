from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.TestFun, name='test'),
    path('welcome/', views.WelcomeFun, name='welcome'),
    path('flipmart/', views.FlipmartFun, name='flipmart'),
    path('adminindex/', views.adminIndexFun, name='adminindex'),
    path('adminhome/', views.adninHomeFun, name='adminhome'),
    # path('gallery/', views.GalleryFun, name='gallery'),
    # path('dashboard/', views.DashboardFun, name='dashboard'),
    # path('staff/', views.StaffFun, name='staff'),
    # path('rooms/', views.RoomsFun, name='rooms'),

    path('signup/', views.fnsignup, name='signup'),
    path('login/',views.fnlogin, name='login'),

    
]
from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from random import random
from myapp.models import *
from django.core.files.storage import FileSystemStorage

# Create your views here.
def TestFun(request):
    return HttpResponse('i am first hotelmanagement')
def WelcomeFun(request):
    return render(request,'welcome.html')
def FlipmartFun(request):
    return render(request,'flipmart.html')
def adminIndexFun(request):
    return render(request,'adminIndex.html')
def adninHomeFun(request):
    return render(request,'adminHome.html')
# def GalleryFun(request):
#     return render(request,'gallery.html')
# def DashboardFun(request):
#     return render(request,'dashboard.html')
# def StaffFun(request):
#     return render(request,'staff.html')
# def RoomsFun(request):
#     return render(request,'rooms.html')

def fnsignup(request):
    try:
        email=request.POST['email']
        objemail=adminRegistration.objects.filter(email_mobile=email).exists()
        print(objemail)
        print("function check")
        if objemail==False:
            firstName=request.POST['fname']
            lastName=request.POST['lname']
            password=request.POST['password']
            dob=request.POST['dob']
            gender=request.POST['gender']
            address=request.POST['address']
            city=request.POST['city']
            state=request.POST['state']
            print("state check")
            file1=request.FILES['pf']
            file2=str(random())+file1.name
            objimg=FileSystemStorage()
            objimg.save(file2,file1)
            print(firstName,lastName,email,password,dob,gender,address,city,state,file1)
            obj=adminRegistration(firstname=firstName,lastname=lastName,email_mobile=email,password=password,dob=dob,gender=gender,address=address,city=city,state=state,file=file2)
            obj.save()
            return render(request,'adminIndex.html',{'msg':'successfully'})
    except Exception as e:print(e)
    return render(request,'adminIndex.html')


# admin login
def fnlogin(request):
    try:
        user=request.POST['email']
        passw=request.POST['password']
        obj=adminRegistration.objects.get(email_mobile=user,password=passw)
        print(obj)
        # session
        request.session['facebooksession']=obj.id
        return render(request,'adminHome.html',{'user':obj.firstname})
    except Exception as e:print(e)
    return render(request,'adminIndex.html',{"msg1":"invalid usernema or password"})





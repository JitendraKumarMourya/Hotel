# from django.http import request
# from django.http.response import HttpResponse
# from django.shortcuts import render
# from django.http import HttpResponse


from os import name
from django.shortcuts import render
from django.http import HttpResponse

from hotelapp.models import addHotels, hoteldetails
from . models import *
from random import random
from django.contrib import messages
from userapp.models import userRegistration
from django.core.files.storage import FileSystemStorage
from . models import userRegistration
# import psycopg2

# Create your views here.
def UserFun(request):
    return HttpResponse('i am userapp')
def HomeFun(request):
    print("Hotel details")
    hotelDetailsta=hoteldetails.objects.all()
    # print(hotelDetailsta)
    

    return render(request,'home.html',{"hotelDetails":hotelDetailsta})


# signup
def fnsignup(request):
    try:
        email=request.POST['email']
        objemail=userRegistration.objects.filter(email_mobile=email).exists()
        
        if objemail==False:
            firstName=request.POST['fname']
            lastName=request.POST['lname']
            password=request.POST['password']
            dob=request.POST['dob']
            gender=request.POST['gender']
            address=request.POST['address']
            city=request.POST['city']
            state=request.POST['state']
            file1=request.FILES['f']
            # print("file read")
            # print(file1.name)
            file2=str(random())+file1.name
            # print(file2)
            objimg=FileSystemStorage()
            objimg.save(file2,file1)
            # obj1=userRegistration(file=file2)
            # obj1.save()
            # objshow.save()
            
            print(firstName,lastName,email,password,dob,gender,address,city,state,file2)
            obj=userRegistration(firstname=firstName,lastname=lastName,email_mobile=email,password=password,dob=dob,gender=gender,address=address,city=city,state=state,file=file2)
            obj.save()
            
            
            messages.success(request,"Created account successfully !!! Thank you")
            return render(request,'home.html')

    except Exception as e:print(e)
    messages.error(request,"user already have an account with this Gmail ID...Sorry !!!")
    return render(request,"home.html")


# login user
def fnlogin(request):
    context={"name":"firstName"}
    try:
        user=request.POST['email']
        passw=request.POST['password']
        obj=userRegistration.objects.filter(email_mobile=user,password=passw).exists()
        if obj:
            data=userRegistration.objects.get(email_mobile=user,password=passw)
            request.session['hotelsession']=data.id
            print(request.session['hotelsession'])
            messages.success(request,"User login successfull !!!")
            # return render(request,'userLoginMaster.html',{"usermsg":data})
            return render(request,'home.html')

        else:
            messages.error(request,"Invalid User name and Password !!!")
            return render(request,'home.html',context)
    except Exception as e:print(e)


def fnuserLoginMaster(request):
    return render(request,'userLoginMaster.html')

# update
def fnuserUpdate(request):
    try:
        user_id=request.session['hotelsession']
        user_data=userRegistration.objects.get(id=user_id)
        
        if request.method=='POST':
            firstname=request.POST['fname']
            lastname=request.POST['lname']
            email_mobile=request.POST['email']
            dob=request.POST['dob']
            gender=request.POST['gender']
            address=request.POST['address']
            city=request.POST['city']
            state=request.POST['state']
            print("half way")
            fle=request.FILES['Full']
            # print(file)
            print(firstname)
            userRegistration.objects.filter(id=user_id).update(firstname=firstname,lastname=lastname,email_mobile=email_mobile,dob=dob,gender=gender,address=address,city=city,state=state,file=fle)
            # print(user_data.firstname,user_data.lastname,user_data.email_mobile,user_data.dob,user_data.gender,user_data.address,user_data.city,user_data.state,user_data=fle)
            # print("successfully update")
            messages.info(request,"Update profile successfully")
    except Exception as e:print(e)
    return render(request,'userUpdate.html')

# chanage Password
def fnchangePass(request):
    try:
        userid=request.session['hotelsession']
        userobj=userRegistration.objects.get(id=userid)
        oldpass=request.POST['oldpass']
        newpass=request.POST['newpass']
        if(userobj.password==oldpass):
            userobj.password=newpass
            userobj.save()
            return render(request,'userChanagePass.html',{'passmsg':'password change successfully !!'})
        return render(request,'userChanagePass.html',{'passmsg':'password change successfully !!'})
    except Exception as e:print(e)
    return render(request,'userchangepass.html')

def fnuserLogout(request):
    try:
        del request.session['hotelsession']
        messages.success(request,"User Logout successfully")
        return render(request,'home.html')
    except Exception as e:print(e)
    

def fnuserDelete(request):
    u_id=request.session['hotelsession']
    delobj= userRegistration.objects.get(id=u_id).delete()
    messages.info(request,"Deleted account successfully")
    return render(request,'home.html')



# Index (Home)
def indexFun(request):
    return render(request,'index.html')









def masterHomeFn(request):
    return render(request,'master_home.html')

def contactFn(request):
    return render(request,'contact.html')

def aboutFn(request):
    return render(request,'about.html')

def searchroomsFn(request):
    allhotels=addHotelsMD.objects.all()
    return render(request,"searchrooms.html",{'addhotels':allhotels})

def fnfilterprice(request):
    return render(request,"searchRoom.html")



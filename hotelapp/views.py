from os import name
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from random import random
from userapp.models import userRegistration
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from hotelapp import views
# Create your views here.

def fnhoteltest(request):
    return HttpResponse('hello hoteltest')

# Admin Registration
def adminsignupFn(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        dob=request.POST['dob']
        email=request.POST['email']
        password=request.POST['password']
        mobile=request.POST['mobile']
        address=request.POST['address']
        pfile=request.POST['pfile']

        obj=hotelappAdmin(firstname=fname,lastname=lname,email=email,dob=dob,password=password,mobile=mobile,address=address,profile=pfile)
        obj.save()
        print("inserted data successfully")
        messages.success(request, "account created successfully")
    return render(request,'base.html')

# admin Login
def adminloginFn(request):
    user=request.POST['email']
    password=request.POST['password']
    obj=hotelappAdmin.objects.filter(email=user,password=password)
    if obj:
        print("checkcondition")
        data=hotelappAdmin.objects.get(email=user,password=password)
        print(data)
        
        request.session['hoteladminsession']=data.id
        print(request.session['hoteladminsession'])
        messages.success(request, "login successfully")
        return render(request,'hotel_admin_home.html',{"userdetails": data})

    else:
        messages.error(request,"Invalid User email and Password !!!")
    return render(request,"base.html")

# Admin logout
def adminlogoutFn(request):
    del request.session['hoteladminsession']
    messages.success(request,"User Logout successfully")
    return render(request,'base.html')


def baseFn(request):
    return render(request,'base.html')

def homeFn(request):
    # details=hoteldetails.objects.all()
    return render(request,'hotel_admin_home.html')


    # book room (Hotelapp)
def fnBookRoom(request):
    if request.method=='POST':
        
        # if request.POST['sel_dlx']!='Room Type':

        #    selected="Delux"
        # else:
        #     selected="Standard"
        # print(selected)
        firstname=request.POST['fstname']
        lastname=request.POST['lstname']
        email=request.POST['mail']
        mobile=request.POST['mob']
        address=request.POST['add']
        city=request.POST['cty']
        state=request.POST['st']
        check_in_date=request.POST['ck_in_date']
        check_in_time=request.POST['ck_in_time']
        check_out_date=request.POST['ck_out_date']
        check_out_time=request.POST['ck_out_time']
        roomtype=request.POST['rd']
        adults=request.POST['adult']
        children=request.POST['child']
        idtype=request.POST['id_type']
        roombook_obj=bookRoom(FirstName=firstname,LastName=lastname,Email=email,Mobile=mobile,Address=address,City=city,State=state,CheckInDate=check_in_date,CheckInTime=check_in_time,CheckOutDate=check_out_date,CheckOutTime=check_out_time,RoomType=roomtype,Adults=adults,Childrens=children,IdType=idtype)
        roombook_obj.save()
        print("Room Booked Successfully")
       
        return render(request,'/userapp/home.html',{'msg':'Room Booked Successfully'})
    return render(request,'/userapp/home.html')

# def fnRoomPrice(request):
#     singleroom_ac=request.POST['']
#     singleroom=request.POST['']
#     doubleroom_ac=request.POST['']
#     doubleroom=request.POST['']
#     roomprice_obj=roomPrice(SingleRoom_WithAC=singleroom_ac,SingleRoom=singleroom,DoubleRoom_WithAC=doubleroom_ac,DoubleRoom=doubleroom)
#     roomprice_obj.save()
    
#     return render(request,'/userapp/home.html')

def addhotelFn(request):
    details=hoteldetails.objects.all()
    
    try:
        if request.method=='POST':
            
            file_1=request.FILES['img']
            print(file_1)
            file_2=str(random())+file_1.name
            objimg=FileSystemStorage()
            objimg.save(file_2,file_1)
            hotelname=request.POST['hotelname']
            hotellocation=request.POST['hotellocation']
            hoteldesc=request.POST['hoteldescription']
            objaddhotel=hoteldetails(hotelimage=file_2,hotelname=hotelname,hoteldescription=hoteldesc,hotellocation=hotellocation)
            objaddhotel.save()
            print(details)
            print("hotel add successfully")
            messages.success(request,"Room Add successfully")
    except Exception as e:print(e)
    return render(request,'addhotel.html',{'alldata':details})


# ( add new Hotel)
def addnewhotelFn(request):

    try:
        if request.method=='POST':
            file1=request.FILES['hotelimage']
            file2=str(random())+file1.name
            imgobj=FileSystemStorage()
            imgobj.save(file2,file1)
            hotelname=request.POST['hotelname']
            hotellocation=request.POST['hotellocation']
            hoteldescription=request.POST['hoteldescription']
            print(hotelname,hotellocation,hoteldescription)
            obj=addHotels(hotelimage=file2,hotelname=hotelname,hotellocation=hotellocation,hoteldescription=hoteldescription)
            obj.save()
            print("added hotel sucessfully...")
        if request.method == 'GET':
            allhotel=addHotels.objects.all()
            return render(request,'addnewhotel.html',{'hoteldata':allhotel})
    except Exception as e:print(e)
    return render(request,'addnewhotel.html')


def addnewroomsFn(request):
    return render(request,"addnewrooms.html")
    













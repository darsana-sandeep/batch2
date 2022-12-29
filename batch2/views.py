from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from batch2.form import ProfileForm, StudentForm, RegisterForm, TeacherForm, NewStudentForm, UserImageForm
from batch2.functions.functions import handle_uploaded_file
from batch2.models import Member, Registrations, Newdata, Newdata1
import requests


def data(request):
    members = Member.objects.all()
    return render(request,"data.html",{"members":members})

def create(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        mem = Member.objects.create(first_name=fname,last_name=lname)
        mem.save()
        return redirect('/')


def delete(request,id):
    mems = Member.objects.get(id=id)
    mems.delete()
    return redirect('/')

def Edit(request,id):
    mem = Member.objects.get(id=id)
    return render(request,'edit.html',{"member":mem})


def update(request,id):
    member = Member.objects.get(id=id)
    member.first_name = request.POST['firstname']
    member.last_name = request.POST['lastname']
    member.save()
    return redirect('/')

# def registration(request):
#
#     if request.method == 'POST':
#         fname = request.POST['firstname']
#         lname = request.POST['lastname']
#         email = request.POST['email']
#         uname = request.POST['username']
#         pswd = request.POST['passwd']
#         cpswd = request.POST['cpasswd']
#
#         data = Registrations.objects.filter(username=uname)
#         print(data)
#         if data:
#             return HttpResponse("username already")
#         else:
#
#             if pswd == cpswd :
#                     user_data = Registrations.objects.create(fname=fname,lname=lname,email=email,username=uname,password=pswd)
#                     user_data.save()
#                     return redirect(login)
#             else:
#                     return HttpResponse("password not matching")
# #
# #
#     return render(request,"registration.html")
# #
# def login(requset):
#     if requset.method == 'POST':
#         uname = requset.POST['username']
#         pswd = requset.POST['passwd']
#
#         data = Registrations.objects.filter(username = uname,password =pswd)
#         if data:
#             requset.session['user'] = uname
#             return redirect('/')
#         else:
#             return HttpResponse("Please enter a valid username and password")
#     return render(requset,'login.html')
# #

def teacherdata(request):
    form = TeacherForm()
    return render(request,'teacher.html',{'form':form})
#
#
def registration(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        uname = request.POST['username']
        pswd = request.POST['passwd']
        cpswd = request.POST['cpasswd']

        data = Registrations.objects.filter(username = uname)

        if data :
            return HttpResponse("Username already exist")
        else:
            if pswd == cpswd:
                user_data = Registrations.objects.create(fname=fname,lname=lname,email=email,username=uname,password=pswd)
                user_data.save()
                return redirect(login)

            else:
                return HttpResponse("Password and confirm password are not matching")
    return render(request, "registration.html")


# def login(request):
#     if request.method == 'POST':
#         uname = request.POST['username']
#         pswd = request.POST['passwd']
#
#         data = Registrations.objects.filter(username = uname,password = pswd)
#         if data:
#             return redirect('/')
#
#         else:
#             return HttpResponse("Please enter a valid username and password")
#
#
#     return render(request, "login.html")


def profile(request):
    form = StudentForm()
    print(form)
    return render(request,"profile.html",{'form':form})


# def UserRegister(request):
#     form = UserCreationForm()
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(login)
#     return render(request,'reg.html',{"form":form})


def UserRegister(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(userlogin)
    return render(request,'reg.html',{"form":form})

def userlogin(request):
    if request.method == 'POST':
         uname = request.POST['username']
         pswd = request.POST['passwd']
         user = authenticate(username=uname, password=pswd)
         if user is not None:
             login(request, user)
             print(request.user.username)
             return redirect(NewFunct)
         else:

             return redirect(userlogin)
             return HttpResponse('<h1>invalid username or password</h1>')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect(userlogin)


def indexdata(request):
    if request.method == 'POST':
        student = NewStudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
    else:
        student = NewStudentForm()
        return render(request,"newform.html",{'form':student})


def image_request(request):
    form = UserImageForm()
    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Getting the current instance object to display in the template
            img_object = form.instance

            return render(request, 'imgform.html', {'form': form, 'img_obj': img_object})

    return render(request, 'imgform.html', {'form': form})

def NewFunct(requset):
    if requset.method == 'POST':
        name = requset.POST['fname']
        data = Newdata1.objects.create(name=name,user_id=requset.user.id)
        data.save()
        print(data)
    return render(requset,"newform.html")

def SendOTP(request):

    if request.method == 'POST':
        phone = request.POST['phone']
        url = f"https://2factor.in/API/V1/482e2bfc-3db4-11ed-9c12-0200cd936042/SMS/+91{str(phone)}/AUTOGEN/OTP1"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)
    return render(request,'sendotp.html')

def VerifyOTP(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        otp = request.POST['otp']

        url = "https://2factor.in/API/V1/482e2bfc-3db4-11ed-9c12-0200cd936042/SMS/VERIFY3/91{0}/{1}".format(phone,otp)

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        res = response.json()
        if res['Status'] == "Success":
            return HttpResponse("successfully verified")
        else:
            return HttpResponse("verification failed")

    return render(request,'verifyotp.html')


def new_function(requset):
    pass
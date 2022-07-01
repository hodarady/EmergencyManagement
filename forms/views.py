from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages
from .forms import Form1 , Form2
import pytz
import datetime

from .models import ModelForm1 , profiles
import datetime

loggend = [False]
usernames = ['muhammed']
@csrf_exempt
def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        usernames[0] = username
        password = request.POST["password"]
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request , user)
            loggend[0] = True
            return redirect("services")
        else:
            messages.success(request , "Invalid Username or Password")
            return redirect("signin")
    return render(request , 'forms/signin.html')

def _logout(request):
    logout(request)
    loggend[0] = False
    return redirect('signin')

def services(request):
    if loggend[0] == False:
        return redirect('signin')
    return render(request , 'forms/services.html')


@csrf_exempt
def form1(request):
    if loggend[0] == False:
        return redirect('signin')
    submitted = False
    if request.method == "POST":
        form = Form1(request.POST)
        if form.is_valid:
            print(request.POST)
            form.save()
        return HttpResponseRedirect("/new_patient?submitted=True")
    else:
        form = Form1
        if 'submitted' in request.GET:
            submitted = True
    return render(request , "forms/new_patient.html" , {"submitted" : submitted})

@csrf_exempt
def form2(request):
    if loggend[0] == False:
        return redirect('signin')
    submitted = False
    if request.method == "POST":
        form = Form2(request.POST)
        print(form)
        if form.is_valid:
            print(request.POST)
            form.save()
        return HttpResponseRedirect("/new_resident?submitted=True")
    else:
        form = Form1
        if 'submitted' in request.GET:
            submitted = True
    return render(request , "forms/add_resident.html" , {"submitted" : submitted})


def display_patients(request):
    if loggend[0] == False:
        return redirect('signin')
    x = ModelForm1.objects.all()
    return render(request , 'forms/table.html' , {"patients" : x})

@csrf_exempt
def search(request):
    if loggend[0] == False:
        return redirect('signin')
    if request.method == "POST":
        NID = request.POST["NID"]
        x = ModelForm1.objects.filter(nationalId = str(NID))
        return render(request , 'forms/table.html' , {"patients" : x})
    else:
        return redirect('display_patients')

def editExitTime(request , pk):
    if loggend[0] == False:
        return redirect('signin')
    x = ModelForm1.objects.get(id = str(pk))
    x.exitDate = datetime.datetime.utcnow()+datetime.timedelta(hours=2)
    x.save()
    return redirect('display_patients')

@csrf_exempt
def invoice(request):
    if request.method == "POST":
        id = request.POST["NID"]
        x = ModelForm1.objects.get(id = str(id))
        time = datetime.datetime.utcnow()+datetime.timedelta(hours=2)
        return render(request , "forms/invoice.html" , {'patient' : x , 'current_date' : time})
    return render(request , "forms/invoice.html")

# def addExitTime(request):
#     if loggend[0] == False:
#         return redirect('signin')
#     return render(request , 'forms/update.html')

def showProfileInfo(request):
    if loggend[0] == False:
        return redirect('signin')
    x = profiles.objects.filter(name = usernames[0])
    if len(x) == 0:
        x = x
    else:
        x = x[0]
    return render(request , 'forms/user_profile.html' , {'Profiles' : x})

def rooms(request):
    if loggend[0] == False:
        return redirect('signin')

    patients = ModelForm1.objects.filter(exitDate = None)
    all_rooms = {key : value for key , value in zip(range(1 , 13) , [1] * 12)}
    rooms = [patients[i].roomNumber for i in range(len(patients))]

    for key in rooms:
        all_rooms[key] = 0
    print(all_rooms)
    return render(request , 'forms/rooms.html' , {'rooms' : all_rooms})

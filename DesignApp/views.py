from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
from django.db import models
from DesignApp.models import User_Details,Building_Details
from .formschool import SchoolForm
from .formhouse import HouseForm
import random
def home_view(request,*args,**kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,"./pages/home.html",context={},status=200)
  
def UserList_view(request,*args,**kwargs):
    qs = User_Details.objects.all()
    UserList = [{"Type":x.Type,"Area":x.Area,"Runs":random.randint(0, 12333333333333)} for x in qs]
    data = {
        "List":UserList
    }
    return JsonResponse(data)


def Building_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "./pages/Buildings.html", context={}, status=200)

def BuildingList_view(request, *args, **kwargs):
    qs = Building_Details.objects.all()
    UserList = [{"Description": x.Description, "Area": x.Area,"Height": x.Height} for x in qs]
    data = {
        "List2": UserList
    }
    return JsonResponse(data)

def SchoolCreateView(request,*args, **kwargs):

    form = SchoolForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = SchoolForm()
    return render(request,"./components/formschool.html",context={"form":form})


def HouseCreateView(request, *args, **kwargs):

    form = HouseForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = HouseForm()
    return render(request, "./components/formhouse.html", context={"form": form})


def DesignApp_view(request,user_id,*args,**kwargs):
    
    data = {
        "Design_id": user_id,
        
    }
    status = 200
    try:
        obj = User_Details.objects.get(id=user_id)
        data["Type"] = obj.Type
        data["Area"] = obj.Area
    except:
        data["Message"] = "Not found"
        status = 404
    
    return JsonResponse(data,status = status)







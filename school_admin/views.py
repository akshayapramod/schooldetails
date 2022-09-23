from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'schooltemplates/home.html')
def viewstaff(request):
    return render(request,'schooltemplates/viewstaff.html')
def addstaff(request):
    return render(request,'schooltemplates/addstaff.html')
def viewstudent(request):
    return render(request,'schooltemplates/viewstudent.html')

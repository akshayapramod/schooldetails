from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'teachertemplates/home.html')
def addstudent(request):
    return render(request,'teachertemplates/addstudent.html')
def viewstudent(request):
    return render(request,'teachertemplates/viewstudent.html')
def changepassword(request):
    return render(request,'teachertemplates/changepassword.html')
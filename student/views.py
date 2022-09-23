from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'studenttemplates/home.html')
def profile(request):
    return render(request,'studenttemplates/profile.html')
def changepassword(request):
    return render(request,'studenttemplates/changepassword.html')
from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home),
    path('addstudent',views.addstudent),
    path('viewstudent',views.viewstudent),
    path('changepassword',views.changepassword),
]
    
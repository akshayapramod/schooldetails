from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home),
    path('viewstaff',views.viewstaff),
    path('addstaff',views.addstaff),
    path('viewstudent',views.viewstudent),
]
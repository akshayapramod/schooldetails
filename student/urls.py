from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home),
    path('profile',views.profile),
    path('changepassword',views.changepassword),
]
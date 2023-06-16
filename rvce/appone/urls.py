from django.conf.urls import *
from appone import views
from django.urls import path

urlpatterns = [
    path('register',views.register,name = 'register'),
    path('login',views.login_view,name = 'login'),
    path('loginsuccess',views.loginsuccess, name = 'ls'),
    path('ngoregister',views.ngo_register,name = 'ngoregister'),
    path('ngologin',views.ngo_login_view,name = 'ngologin'),
    path('volunteer',views.volunteer),
    path('blogpage',views.blogview),
    path('ngosearch',views.ngosearch),
]
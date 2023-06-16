from django.conf.urls import *
from appone import views
from django.urls import path

urlpatterns = [
    path('register',views.register,name = 'register'),
    path('login',views.login_view,name = 'login'),
    path('ngoportal',views.ngoportal, name = 'ls'),
    path('ngoregister',views.ngo_register,name = 'ngoregister'),
    path('ngologin',views.ngo_login_view,name = 'ngologin'),
    path('volunteer',views.volunteer),
    path('blogpage',views.blogview),
    path('ngosearch',views.ngosearch),
    path('dropdown',views.dropdown_view),
    path('newblog',views.newblog),
    path('ngoportal',views.ngoportal)
]
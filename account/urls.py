from django.urls import path,include
from django.contrib import admin
from . import views
urlpatterns = [
    path('register/',views.userregister,name='register'),
    path('create-store',views.create_store,name='create_store'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.logoutuser,name='logout'),


]


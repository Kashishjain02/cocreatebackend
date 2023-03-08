from django.urls import path
from . import views

urlpatterns = [
    path('create_subscription/', views.create_subscription, name='create_subscription'),
    path('test/', views.test, name='test'),
]
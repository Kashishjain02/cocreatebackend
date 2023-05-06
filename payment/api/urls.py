from django.urls import path
from . import views
urlpatterns = [
    path('create_payment_order/', views.create_payment_order, name='create_payment_order'),
    path('payment-handler/', views.payment_handler, name='payment_handler'),
    path('payment-success/', views.payment_success, name='payment_success'),
]
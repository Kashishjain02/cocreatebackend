from django.urls import path
from . import views

urlpatterns = [
    path('create_subscription/', views.create_subscription, name='create_subscription'),
    path('test/', views.test, name='test'),
    path('subscription-handler/', views.subscription_handler, name='subscription_handler'),
    path('create_payment_order/', views.create_payment_order, name='create_payment_order'),
    path('payment-handler/', views.payment_handler, name='payment_handler'),
]
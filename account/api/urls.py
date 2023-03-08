from django.urls import path
from . import views
urlpatterns = [
    path('test/', views.test_api, name='test-api'),
    path('mentordata/', views.mentor, name='mentordata'),
    path('mentordata/<int:id>', views.mentor, name='mentordata'),
    # path('startupdata/', views.startup, name='startupdata'),
    # path('startupdata/<int:id>', views.startup, name='startupdata'),
    path('register/', views.user_registration, name='register'),

]
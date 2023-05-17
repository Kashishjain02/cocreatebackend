from django.urls import path
from . import views
urlpatterns = [
    path('mentortest/', views.test_api, name='mtest-api'),
    path('apply-for-mentorship/', views.apply_for_mentorship, name='apply-mentorship'),
    path('application-info/', views.application_info, name='application-info'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='Newapp'),
    path('check_user/',views.check_user,name='check_user'),
]

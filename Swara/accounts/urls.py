from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('manageaccount/', views.manageaccount),
    path('profilepage/', views.profilepage),
]


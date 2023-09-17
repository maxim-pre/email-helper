from rest_framework.urls import path 
from . import views


urlpatterns = [
    path('auth/callback', views.get_access_key)
]
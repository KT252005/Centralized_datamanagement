from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name="login"),
    path('signup.html',views.registration,name="sign_up"),
    path('access.html',views.access,name="access"),
    path('login.html',views.home),
    
]
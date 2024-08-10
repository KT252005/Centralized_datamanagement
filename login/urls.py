from django.urls import path,include 
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
urlpatterns = [
    path('',views.home,name="login"),
    path('signup.html',views.registration,name="sign_up"),
    path('access.html',views.access,name="access"),
    path('login_user',views.login_user,name="login_user"),
    path('rest-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest/', include(router.urls)),
    
]
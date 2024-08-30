from django.urls import path,include 
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'organization',views.Organizationviewset)
urlpatterns = [
    path('',views.home,name="login"),
    path('signup.html',views.registration,name="sign_up"),
    path('dashboard.html',views.access,name="access"),
    path('login_user',views.login_user,name="login_user"),
    path('rest-auth/', include('rest_framework.urls', namespace='backend_testing')),
    path('rest/', include(router.urls)),
    
]

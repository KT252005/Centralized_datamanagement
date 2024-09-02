from django.urls import path,include 
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'organization',views.Organizationviewset)
urlpatterns = [
    path('login/',views.home,name="login"),
    path('signup.html',views.signup,name="sign_up"),
    path('',views.access,name="access"),
    # routing the register function
    path('Registration.html/',views.organization_dash,name="org_dash"),
    path('fund.html/',views.fund,name="fund"),
    path('login_user',views.login_user,name="login_user"),
   
    path('rest/', include(router.urls)),
#     path('api/user/<str:username>/profile', user_info_api, name='user-info-api'),
    
]

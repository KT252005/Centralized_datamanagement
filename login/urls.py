from django.urls import path,include 
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'allocation',views.AllocationViewSet)
urlpatterns = [
    path('login/',views.home,name="login"),
    path('signup/',views.registration,name="sign_up"),
    path('',views.access,name="access"),
    path("user/",views.user,name="user"),
    # routing the register function
    path('registration/',views.organization_dash,name="org_dash"),
    path('fund/',views.fund,name="fund"),
    path('login/login_user',views.login_user,name="login_user"),
    path("startup/",views.startup_page,name="startup_page"),
    path("projects/",views.projects_page,name="project_page"),
    path('rest/', include(router.urls)),
#     path('api/user/<str:username>/profile', user_info_api, name='user-info-api'),
    
]

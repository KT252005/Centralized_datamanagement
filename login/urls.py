from django.urls import path,include 
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'allocation',views.AllocationViewSet)
urlpatterns = [
    path('login/',views.login,name="login"),
    path('signup/',views.registration,name="sign_up"),
    path('',views.home,name="Home"),
     path('login/home/',views.home_new,name="login_home"),

    # routing the register function
    # path('registration/',views.organization_dash,name="org_dash"),
    path('fund/',views.fund,name="fund"),
    path('login_user/',views.login_user,name="login_user"),
    path("startup/",views.startup_page,name="startup_page"),
    path("projects/",views.projects_page,name="project_page"),
    path("profile/",views.profile_view,name="profile"),
    path("profile/details/edit",views.details_form,name="details_form"),
    path("ipr/",views.ipr,name="ipr"),
    path("patent/",views.patent,name="patent"),
    path("login/home/new",views.home_new,name="home_new"),
    # path('api/user-profile/<int:user_id>/',views.profile_view ,name="profile_view"),
    

    #for api testing
    path('rest/', include(router.urls)),
#     path('api/user/<str:username>/profile', user_info_api, name='user-info-api'),
    
]

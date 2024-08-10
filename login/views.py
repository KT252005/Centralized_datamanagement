from django.shortcuts import render, redirect,HttpResponse
from .forms import SignupForm
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User,Group
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import tutorial.quickstart
from tutorial.quickstart.serializers import GroupSerializer, UserSerializer
from rest_framework import viewsets,permissions
from django.contrib.auth.hashers import make_password,check_password






# Create your views here.
def home(request):
    return render(request,"index.html")

def access(request):
      return render(request,"access.html")

def registration(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.password = make_password(form.cleaned_data['password']) 
            user.save()
            return redirect('login')
        else:
            return render(request, 'base.html', {'form': form})   
    else:
        return render(request, 'base.html', {'form': form})   
    

def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user_type = data['role']
        
        try:
            user = Chat_signup.objects.get(username=username)
            if check_password(password, user.password) and user.role == user_type:
                # Mock login by setting session or token
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                request.session['role'] = user.role
                if user_type == 'user':
                    return JsonResponse({'success': True, 'redirect_url': 'access.html'})
                elif user_type == 'admin':
                    return JsonResponse({'success': True, 'redirect_url': '/admin/'})
                else:
                    return JsonResponse({'success': False, 'error': 'Invalid user type'})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid credentials or user type'})
        except Chat_signup.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User does not exist'})
               
    return render(request,'login.html')             


#****api****
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
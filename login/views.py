from django.shortcuts import render, redirect,HttpResponse
from .forms import SignupForm
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User,Group
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .Serializers import AllocationSerializer
import tutorial.quickstart
from tutorial.quickstart.serializers import GroupSerializer, UserSerializer
from rest_framework import viewsets,permissions
from django.contrib.auth.hashers import make_password,check_password
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404  # Add get_object_or_404 here

# render  functions


def home_new(request):
    return render(request,"login_home.html")

def ipr(request):
    return render(request,"ipr.html")


def fund(request):
    return render(request,"fund.html")

def login(request):
    return render(request,"index.html")

def home(request):
      return render(request,"Home_Dashboard.html")


def startup_page(request):
    return render(request,"startup.html")

def  projects_page(request):
    return render(request,"project.html")

# def profile(request):
#     return render(request,"viewprofile.html")


def patent(request):
    return render(request,"patent.html")

def  details_form(request):
    return render(request,"details_profile.html")
#from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
import json

# @csrf_exempt  # Ensure to handle CSRF manually in the frontend
def organization_dash(request):
    if request.method == 'POST':
        try:
            # Extract data from form submission using request.POST
            gst_no = request.POST.get('gst')
            company_name = request.POST.get('company-name')  # Use the key as it is in the form
            domain = request.POST.get('domain')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            pincode = request.POST.get('pincode')
            contact_info = request.POST.get('contact')

            print(f"Extracted values: gst={gst_no}, company_name={company_name}, domain={domain}, address={address}, city={city}, state={state}, pincode={pincode}, contact={contact_info}")

            # Save data to the model
            organization = Organizations_data.objects.create(
                Gst_no=gst_no,
                Company_name=company_name,
                Domain=domain,
                Address=address,
                city=city,
                State=state,
                Pincode=pincode,
                contact_info=contact_info
            )
            organization.save()


            # Return a success response
            # Inside your Django view
            # redirect_url = reverse('login') 
            # return JsonResponse({'success': True, 'redirect_url': redirect_url})
            messages.success(request, 'Organization created successfully!')

            return redirect('access') 
        except Exception as e:
            # Handle other errors
            return JsonResponse({'success': False, 'error': str(e)})

    # Render the form if it's a GET request
    return render(request, "Registration.html")


def registration(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.password = make_password(form.cleaned_data['password']) 
            user.save()
            return redirect('/login/')
        else:
            return render(request, 'base.html', {'form': form})   
    else:
        return render(request, 'base.html', {'form': form})   
    

def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        username = data['username']
        password = data['password']
        user_type = data['role']
        
        try:
            user = signup_data.objects.get(username=username)
            if check_password(password, user.password) and user.role == user_type:
                # Mock login by setting session or token
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                request.session['role'] = user.role
                
                
                print(request.session.items())
                
                if user_type == 'user':
                    return JsonResponse({'success': True, 'redirect_url': 'home/new'})
                elif user_type == 'admin':
                    return JsonResponse({'success': True, 'redirect_url': '/admin/'})
                else:
                    return JsonResponse({'success': False, 'error': 'Invalid user type'})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid credentials or user type'})
        except signup_data.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User does not exist'})
               
    return render(request,'base.html')             


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
    
    
# class Organizationviewset(viewsets.ModelViewSet):
#     queryset=Organizations_data.objects.all().order_by('Gst_no','Company_name','Domain','Address','city','State','Pincode','contact_info')    
#     serializer_class=Organizations_Serializer
    
class AllocationViewSet(viewsets.ModelViewSet):
      queryset=Allocation.objects.all().order_by('user',
            'Startup_name',
            'contact_info',
            'created_at',
            'updated_at')    
      serializer_class=AllocationSerializer
    
# def user_info_api(request, username):
#     try:
#         user = signup_data.objects.get(username=username)
#         company_name=[org.Company_name  for org in user.organizations.all()]
#         data = {
#             'name': f"{user.first_name} {user.last_name}",
#             'company_name': company_name,
#             'email': user.email,
#         }
#         return JsonResponse(data,status=200)
#     except signup_data.DoesNotExist:
#         return JsonResponse({'error': 'User not found'}, status=404)    



def profile_view(request):
    # for user_id and username are in session retrieve and send to destination html with parameter
    if 'user_id' in request.session and 'username' in request.session:
        user_id = request.session['user_id']
        username = request.session['username']
        
        try:
            user = signup_data.objects.get(id=user_id)
            
            data = {
                "username": user.username,
                "email": user.email,
            }
            return render(request, 'viewprofile.html', data)
        
        except signup_data.DoesNotExist:
            return JsonResponse({'error': 'User not found'})
    else:
        # If session data is missing, redirect to login or show an error
        return JsonResponse({'error': 'User is not logged in'})

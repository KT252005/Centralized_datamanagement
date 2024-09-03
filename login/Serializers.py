from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import  Allocation , funding

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
# class Organizations_Serializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Organizations_data
#         fields = [
#             'url',
#             'Gst_no',
#             'Company_name',
#             'Domain',
#             'Address',
#             'city',
#             'State',
#             'Pincode',
#             'contact_info',
#             'created_at',
#             'updated_at'
#         ]
        
class AllocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allocation
        fields = [
            'user',
            'Startup_name',
            'contact_info',
            'created_at',
            'updated_at'
        ]        
 
 
class    fundingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = funding
        fields = [
            'user',
            'Startup_name',
            'Amount',
            'Amount_used',

        ]        
 
from rest_framework import serializers
from crud.models import *

class UserregSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userregister
        fields = ('id','f_name','l_name','dob','gender','email')


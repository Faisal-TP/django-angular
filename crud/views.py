from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from crud.models import *
from crud.serializers import UserregSerializer
# Create your views here.

@csrf_exempt
def addfn(request,id=0):
    if request.method=='GET':
        User = Userregister.objects.all()
        user_serializer = UserregSerializer(User,many='True')
        return JsonResponse(user_serializer.data,safe=False)
    elif request.method=='POST':
        userdata = JSONParser().parse(request)
        user_serializer = UserregSerializer(data = userdata)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse('Data inserted Successfully..!',safe=False)
        return JsonResponse('Failed to register..!',safe=False)
    elif request.method=='PUT':
        userdata = JSONParser().parse(request)
        user = Userregister.objects.get(id=userdata['id'])
        user_serializer = UserregSerializer(user,userdata)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse('Data updated Successfully..!',safe=False)
        return JsonResponse('Failed to update..!',safe=False)
    elif request.method=='DELETE':
        user = Userregister.objects.get(id=id)
        user.delete()
        return JsonResponse('Data deleted Successfully..!',safe=False)



    


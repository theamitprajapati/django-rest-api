from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EmpModel
from .serializer import MyTokenObtainPairSerializer,UserSerializer
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate



from django.contrib.auth.models import User


# Create your views here.
@api_view(['GET'])
def welcome(request):
    return Response({
        'login':"http://localhost:8000/login",
        'register':"http://localhost:8000/register",
        'reset-password':"http://localhost:8000/reset-password",
        'change-password':"http://localhost:8000/change-password",
        'forget-password':"http://localhost:8000/forget-password",
    })

@api_view(['POST'])
def login(request):
    try:
        row = dict(request.data)    
        user = authenticate(request,username=row['username'],password=row['password'])
        if user is None:
            return Response({"response":"Invalid Username or Password"})
        
        data = MyTokenObtainPairSerializer.get_token(user)
        name = user.first_name + ' ' + user.last_name
        return Response({'name':name,"email":user.email,"token":data},status=status.HTTP_200_OK)

    except Exception:
        return Response({"response":"Somethink went wrong"})

    # user = serializer.data
    # data = MyTokenObtainPairSerializer.get_token(user)
    # if user['password'] == row['password']:
    #     return Response({'name':user['name'],"token":data},status=status.HTTP_200_OK)
    # else:
    return Response({'message':"Invlid email or passowrd"}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def register(request):
    if request.method == 'GET':
        return Response({"error":"Not found get method"})       
    try:
        u = request.data
        user = User(email=u['email'],password=make_password(u['password']),first_name=u['first_name'],last_name=u['last_name'],username=u['username'])
        data = user.save()
        return Response({"message":"Success!"}, status=status.HTTP_201_CREATED)
    except:  
        return Response({"message":'Somethin went wrong?'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list(request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)


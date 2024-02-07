from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EmpModel
from .serializer import DataSerializer

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
    row = dict(request.data)
    #print("Log",row['email'],flush=True)

    details =  EmpModel.objects.get(email=row['email'],password=row['password'])
    serializer = DataSerializer(details)
    print(serializer.data,flush=True)
    # if serializer.is_valid():
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def list(request):
    app = EmpModel.objects.all()
    serializer = DataSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register(request):
    if request.method == 'GET':
        return Response({"error":"Not found get method"})       

    elif request.method == 'POST':
        print(request.data,flush=True)
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# {
#     "email": "admin",
#     "password": "admin"
# }
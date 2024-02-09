from rest_framework import serializers
from .models import EmpModel

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from drf.settings import  SIMPLE_JWT as api_settings


class DataSerializer(serializers.ModelSerializer):
    

    class Meta:

        model=EmpModel

        fields=('name','email','password','description')


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        user = dotdict(user)
        token = super().get_token(user)
        token['name'] = user.name
        return token

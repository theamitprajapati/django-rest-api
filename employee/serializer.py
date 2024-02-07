from rest_framework import serializers
from .models import EmpModel

class DataSerializer(serializers.ModelSerializer):
    

    class Meta:

        model=EmpModel

        fields=('name','email','password','description')

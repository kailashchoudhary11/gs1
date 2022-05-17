from rest_framework import serializers
from .models import Student

# class StudentSerializer(serializers.ModelSerializer):
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    prn = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)
    

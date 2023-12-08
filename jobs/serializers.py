from rest_framework import serializers
from .models import Job , Category , Company 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        
class JobListSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Job
        fields = '__all__'
        
class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


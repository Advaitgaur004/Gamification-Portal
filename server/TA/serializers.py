from rest_framework import serializers
from .models import InstructorProfile, StudentTaskStatus

class InstructorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorProfile
        fields = '__all__'

class StudentTaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTaskStatus
        fields = '__all__'

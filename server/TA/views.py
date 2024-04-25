from rest_framework import viewsets
from .models import InstructorProfile, StudentTaskStatus
from .serializers import InstructorProfileSerializer, StudentTaskStatusSerializer

class InstructorProfileViewSet(viewsets.ModelViewSet):
    queryset = InstructorProfile.objects.all()
    serializer_class = InstructorProfileSerializer

class StudentTaskStatusViewSet(viewsets.ModelViewSet):
    queryset = StudentTaskStatus.objects.all()
    serializer_class = StudentTaskStatusSerializer

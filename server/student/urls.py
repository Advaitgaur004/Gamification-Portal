from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, StudentProfileViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'student-profiles', StudentProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

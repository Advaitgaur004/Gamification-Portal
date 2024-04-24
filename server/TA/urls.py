from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstructorProfileViewSet, StudentTaskStatusViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'instructor-profiles', InstructorProfileViewSet)
router.register(r'student-task-statuses', StudentTaskStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

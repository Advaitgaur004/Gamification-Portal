from django.db import models
from django.contrib.auth.models import User
from student.models import Task, StudentProfile

class InstructorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class StudentTaskStatus(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    earned_xp = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student.user.username} - {self.task.title}"

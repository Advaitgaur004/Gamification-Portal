from django.db import models
from django.contrib.auth.models import User
from student.models import StudentProfile

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    xp_reward = models.IntegerField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title
    
class InstructorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class StudentTaskStatus(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    earned_xp = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student.user.username} - {self.task.title}"

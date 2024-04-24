from django.db import models
from django.contrib.auth.models import User

badge_choices = [
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
    ('Expert', 'Expert'),
]

class Badge(models.Model):
    name = models.CharField(max_length=255, choices=badge_choices, default='Beginner')
    description = models.TextField()

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, unique=True)
    rank_xp = models.IntegerField(default=0)
    badge = models.ManyToManyField(Badge, related_name='badges', blank=True)
    email = models.EmailField(unique=True)
    total_xp = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

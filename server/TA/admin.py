from django.contrib import admin
from .models import InstructorProfile, StudentTaskStatus

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user',)
    ordering = ('user',)

class StudentTaskStatusAdmin(admin.ModelAdmin):
    list_display = ('student', 'task', 'completed', 'earned_xp')
    search_fields = ('student', 'task')
    ordering = ('student', 'task')

admin.site.register(InstructorProfile, InstructorAdmin)
admin.site.register(StudentTaskStatus, StudentTaskStatusAdmin)

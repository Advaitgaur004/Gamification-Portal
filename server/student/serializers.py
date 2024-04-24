from rest_framework import serializers
from .models import StudentProfile, Badge

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'

class StudentProfileSerializer(serializers.ModelSerializer):
       class Meta:
        model = StudentProfile
        fields = '__all__'
        write_only_fields = ('user', 'username', 'rank_xp', 'badge', 'email', 'total_xp')
        read_only_fields = ('id',)
        
    
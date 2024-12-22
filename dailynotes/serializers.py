from rest_framework import serializers
from .models import DailyNote

class DailyNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyNote
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']

from rest_framework import serializers
from .models import Assignment , Subject , Notes

class AssignmentSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()
    class Meta:
        model = Assignment
        fields = '__all__'

class NotesSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()
    class Meta:
        model = Notes
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    assignment_set = AssignmentSerializer(many=True,read_only=True)
    notes_set = NotesSerializer(many=True,read_only=True)
    class Meta:
        model = Subject
        fields = '__all__'
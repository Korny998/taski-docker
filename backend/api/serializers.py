"""Serializers for the Task API."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model."""

    class Meta:
        """Meta class to define model and fields for TaskSerializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')

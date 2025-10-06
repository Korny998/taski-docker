"""Admin configuration for the Task model."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Customize the admin interface for the Task model."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)

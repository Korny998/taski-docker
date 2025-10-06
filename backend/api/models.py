"""Database models for the Task app."""

from django.db import models


class Task(models.Model):
    """
    Model representing a task.

    Contains fields for title, description, and completion status.
    """

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        """Return the string representation of the task."""
        return self.title

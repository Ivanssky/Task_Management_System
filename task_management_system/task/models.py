from datetime import datetime

from django.conf import settings
from django.db import models

from task_management_system.tag.models import Tag


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        null=True,
    )
    PUBLIC = 'PU'
    PRIVATE = 'PR'
    VISIBILITY_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    ]
    visibility = models.CharField(
        max_length=2,
        choices=VISIBILITY_CHOICES,
        default=PRIVATE,
    )

    created_at = models.DateTimeField(
        blank=True,
        null=True,
    )
    completed = models.BooleanField(default=False)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

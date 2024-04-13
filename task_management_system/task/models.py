from datetime import datetime

from django.conf import settings
from django.db import models


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
        default=datetime.now()
    )
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

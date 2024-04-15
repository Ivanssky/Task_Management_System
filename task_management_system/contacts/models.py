from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    user_a = models.ForeignKey('user.User', related_name='user_a_contacts', on_delete=models.CASCADE)
    user_b = models.ForeignKey('user.User', related_name='user_b_contacts', on_delete=models.CASCADE)

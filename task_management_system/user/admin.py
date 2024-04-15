from django.contrib import admin

from task_management_system.tag.models import Tag
from task_management_system.task.models import Task
from task_management_system.user.models import User

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Tag)

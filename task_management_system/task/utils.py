import django_filters
from task_management_system.task.models import Task


class SortByPriority(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['priority'].label = 'Sort by priority'

    class Meta:
        model = Task
        fields = ['priority']


class SortByTag(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['tag'].label = 'Sort by tag'

    class Meta:
        model = Task
        fields = ['tag']
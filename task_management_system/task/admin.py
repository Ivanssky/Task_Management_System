from django.contrib import admin
from .models import Task


class TaskTitleFilter(admin.SimpleListFilter):
    title = 'Title'
    parameter_name = 'title'

    def lookups(self, request, model_admin):
        titles = Task.objects.values_list('title', flat=True).distinct()
        return [(title, title) for title in titles]

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(title=value)


class TaskAdmin(admin.ModelAdmin):
    list_filter = (TaskTitleFilter,)


admin.site.register(Task, TaskAdmin)

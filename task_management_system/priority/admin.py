from django.contrib import admin
from .models import Priority


class PriorityNameFilter(admin.SimpleListFilter):
    title = 'Priority'
    parameter_name = 'priority'

    def lookups(self, request, model_admin):
        return (
            ('high', 'High Priority'),
            ('low', 'Low Priority'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            if value == 'high':
                return queryset.filter(name='High Priority')
            elif value == 'low':
                return queryset.filter(name='Low Priority')


class PriorityAdmin(admin.ModelAdmin):
    list_filter = (PriorityNameFilter,)


admin.site.register(Priority, PriorityAdmin)

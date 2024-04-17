from django.contrib import admin
from .models import Tag


class TagNameFilter(admin.SimpleListFilter):
    title = 'Tag Name'
    parameter_name = 'tag_name'

    def lookups(self, request, model_admin):
        return (
            ('Home', 'Home'),
            ('Work', 'Work'),
            ('Other', 'Other'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(name=value)


class TagAdmin(admin.ModelAdmin):
    list_filter = (TagNameFilter,)


admin.site.register(Tag, TagAdmin)

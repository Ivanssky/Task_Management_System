from django.contrib import admin
from .models import User
from ..contacts.models import Contact


class UsernameFilter(admin.SimpleListFilter):
    title = 'Username'
    parameter_name = 'username'

    def lookups(self, request, model_admin):
        usernames = User.objects.values_list('username', flat=True).distinct()
        return [(username, username) for username in usernames]

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(username=value)


class InContactsFilter(admin.SimpleListFilter):
    title = 'In Contacts'
    parameter_name = 'in_contacts'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Yes'),
            ('no', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            user = request.user
            if value == 'yes':
                return queryset.filter(user_a_contacts__user_b=user)
            elif value == 'no':
                return queryset.exclude(user_a_contacts__user_b=user)


class UserAdmin(admin.ModelAdmin):
    list_filter = (UsernameFilter, InContactsFilter,)


admin.site.register(User, UserAdmin)

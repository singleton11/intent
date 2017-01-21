from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """A custom user admin class"""
    filter_horizontal = ('groups', 'user_permissions')

    readonly_fields = ('last_login', 'date_joined')

    list_display = (
        'email',
        'username',
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login',
        'date_joined'
    )

    fieldsets = (
        (
            _('General information'), {
                'fields': (
                    'email',
                    'username',
                    'first_name',
                    'last_name',
                )
            }
        ),
        (
            _('Settings'), {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (
            _('Permissions'), {
                'fields': (
                    'groups',
                    'user_permissions',
                )
            }
        ),
        (
            _('Additional information'), {
                'fields': (
                    'password',
                    'last_login',
                    'date_joined',
                )
            }
        ),
    )

    add_fieldsets = (
        (
            None, {
                'fields': (
                    'email',
                    'username',
                    'password1',
                    'password2'
                )
            }
        ),
    )

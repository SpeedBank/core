from django.contrib import admin

from .models import ApiToken


@admin.register(ApiToken)
class ApiTokenAdmin(admin.ModelAdmin):
    """Admin customisation for ApiToken model."""

    readonly_fields = ('token', 'date_created', 'date_modified')
    list_display = (
         'owner', 'token', 'date_created', 'date_modified'
    )

from django.contrib import admin
from services.models import Faq, Inquiry, Discussion


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):

    list_display = ('bank', 'question')

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(bank=request.user.profile.bank)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        field = super().formfield_for_foreignkey(db_field, request, **kwargs)

        if request.user.is_superuser:
            return field

        if db_field.name == 'bank':
            field.queryset = field.queryset.filter(id=request.user.profile.bank.id)

        return field


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):

    list_display = ('user', 'bank', 'customer_service', 'question', 'is_resolved')

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(bank=request.user.profile.bank)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        field = super().formfield_for_foreignkey(db_field, request, **kwargs)

        if request.user.is_superuser:
            return field

        if db_field.name == 'bank':
            field.queryset = field.queryset.filter(id=request.user.profile.bank.id)

        if db_field.name == 'user':
            field.queryset = field.queryset.filter(profile__bank=request.user.profile.bank)

        if db_field.name == 'customer_service':
            field.queryset = field.queryset.filter(branch__bank=request.user.profile.bank)

        return field


@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):

    list_display = ('user', 'recipient', 'inquiry')

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(inquiry__bank=request.user.profile.bank)


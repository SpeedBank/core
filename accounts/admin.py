from django.contrib import admin
from accounts.models import (
    Bank, Branch, CustomerService, BankAccount, Profile, BranchReview, CustomerServiceReview,
    BankAccountOpening
)
from django.contrib.auth.models import User

admin.site.unregister(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(profile__bank=request.user.profile.bank)


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):

    list_display = ('name', 'address', 'city', 'state', 'country')


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):

    list_display = ('bank', 'name', 'sort_code', 'address', 'city', 'state', 'country')

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(bank=request.user.profile.bank)


@admin.register(CustomerService)
class CustomerServiceAdmin(admin.ModelAdmin):

    list_display = ('user', 'phone', 'email', 'branch')

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(branch__bank=request.user.profile.bank)


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):

    list_display = ('bank', 'name', 'number', 'speed_number', 'phone')

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(bank=request.user.profile.bank)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

        list_display = ('user', 'email', 'phone')

        def get_queryset(self, request):
            """Limit Pages to those that belong to the request's user."""
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs

            return qs.filter(bank=request.user.profile.bank)


@admin.register(BranchReview)
class BranchReviewAdmin(admin.ModelAdmin):

        list_display = ('branch', 'star', 'message')

        def get_queryset(self, request):
            """Limit Pages to those that belong to the request's user."""
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs

            return qs.filter(branch__bank=request.user.profile.bank)


@admin.register(CustomerServiceReview)
class CustomerServiceReviewAdmin(admin.ModelAdmin):

        list_display = ('customer_service', 'star', 'message')

        def get_queryset(self, request):
            """Limit Pages to those that belong to the request's user."""
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs

            return qs.filter(customer_service__branch__bank=request.user.profile.bank)


@admin.register(BankAccountOpening)
class BankAccountOpeningAdmin(admin.ModelAdmin):

        list_display = ('user', 'bank', 'branch', 'phone', 'email', 'bvn')

        def get_queryset(self, request):
            """Limit Pages to those that belong to the request's user."""
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs

            return qs.filter(branch__bank=request.user.profile.bank)

from django.contrib import admin
from accounts.models import Bank, Branch, CustomerService, BankAccount


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):

    list_display = ('name', 'address', 'city', 'state', 'country')


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):

    list_display = ('name', 'sort_code', 'address', 'city', 'state', 'country')


@admin.register(CustomerService)
class CustomerServiceAdmin(admin.ModelAdmin):

    list_display = ('user', 'phone', 'email', 'branch')


@admin.register(BankAccount)
class CustomerServiceAdmin(admin.ModelAdmin):

    list_display = ('name', 'number', 'speed_number', 'phone')

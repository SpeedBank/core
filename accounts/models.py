from django.db import models
from django.contrib.auth.models import User
from accounts.mixins import TimestampMixin


class Bank(TimestampMixin):
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    banner = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=205)
    country = models.CharField(max_length=205)
    latitude = models.FloatField(blank=True, default=0)
    longitude = models.FloatField(blank=True, default=0)

    def __str__(self):
        return self.name


class Branch(TimestampMixin):
    name = models.CharField(max_length=255)
    sort_code = models.IntegerField()
    banner = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=205)
    country = models.CharField(max_length=205)
    latitude = models.FloatField(blank=True, default=0)
    longitude = models.FloatField(blank=True, default=0)

    def __str__(self):
        return self.name


class CustomerService(TimestampMixin):
    user = models.OneToOneField(User, related_name="customer_service")
    branch = models.ForeignKey(Branch, related_name="customer_services")
    profile_image = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class BankAccount(TimestampMixin):
    user = models.ForeignKey(User, related_name="bank_accounts")
    bank = models.ForeignKey(Bank, related_name="bank_accounts")
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    speed_number = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

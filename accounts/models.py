from django.db import models
from django.contrib.auth.models import User
from accounts.mixins import TimestampMixin
from core.utils import logo_location, banner_location, profile_location
from geoposition.fields import GeopositionField


class Bank(TimestampMixin):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to=logo_location, null=True, blank=True)
    banner = models.ImageField(upload_to=banner_location, null=True, blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=205)
    country = models.CharField(max_length=205)
    location = GeopositionField(null=True)

    def __str__(self):
        return self.name


class Branch(TimestampMixin):
    bank = models.ForeignKey(Bank, related_name="branches")
    name = models.CharField(max_length=255)
    sort_code = models.IntegerField()
    banner = models.ImageField(upload_to=banner_location, null=True, blank=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=205)
    country = models.CharField(max_length=205)
    location = GeopositionField(null=True)

    class Meta:
        verbose_name_plural = "Branches"

    def __str__(self):
        return self.name


class BranchReview(TimestampMixin):
    branch = models.ForeignKey(Branch, related_name="reviews")
    star = models.IntegerField(default=0)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.branch.name


class CustomerService(TimestampMixin):
    user = models.OneToOneField(User, related_name="customer_service")
    branch = models.ForeignKey(Branch, related_name="customer_services")
    profile_image = models.ImageField(upload_to=profile_location, null=True, blank=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class CustomerServiceReview(TimestampMixin):
    customer_service = models.ForeignKey(CustomerService, related_name="reviews")
    star = models.IntegerField(default=0)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.customer_service.user.username


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


class BankAccountOpening(TimestampMixin):
    user = models.ForeignKey(User, related_name="bank_account_openings")
    bank = models.ForeignKey(Bank, related_name="bank_account_openings")
    branch = models.ForeignKey(Branch, related_name="bank_account_openings")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=2)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    religion = models.CharField(max_length=255, blank=True, null=True)
    bvn = models.CharField(max_length=255, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)
    valid_id = models.CharField(max_length=255, blank=True, null=True)
    is_pending = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Profile(TimestampMixin):
    user = models.OneToOneField(User, related_name="profile")
    bank = models.ForeignKey(Bank, related_name="profiles", null=True, blank=True)
    profile_image = models.ImageField(upload_to=profile_location, null=True, blank=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.last_name


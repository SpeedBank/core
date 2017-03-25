from django.db import models
from accounts.mixins import TimestampMixin
from accounts.models import Bank
from django.contrib.auth.models import User
from accounts.models import CustomerService, Branch


class Faq(TimestampMixin):
    bank = models.ForeignKey(Bank, related_name="faqs")
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Inquiry(TimestampMixin):
    user = models.ForeignKey(User, related_name="inquiries")
    customer_service = models.ForeignKey(CustomerService, related_name="inquiries")
    bank = models.ForeignKey(Bank, related_name="inquiries")
    branch = models.ForeignKey(Branch, related_name="inquiries", null=True)
    question = models.TextField()
    is_resolved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Inquiries"

    def __str__(self):
        return self.question


class Discussion(TimestampMixin):
    user = models.ForeignKey(User, related_name="discussions")
    recipient = models.ForeignKey(User)
    inquiry = models.ForeignKey(Inquiry, related_name="discussions")
    message = models.TextField()

    def __str__(self):
        return self.message

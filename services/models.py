from django.db import models
from accounts.mixins import TimestampMixin
from accounts.models import Bank
from django.contrib.auth.models import User


class Faq(TimestampMixin):
    bank = models.ForeignKey(Bank, related_name="faqs")
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class CustomerQuestion(TimestampMixin):
    user = models.ForeignKey(User, related_name="questions")
    bank = models.ForeignKey(Bank, related_name="questions")
    question = models.TextField()

    def __str__(self):
        return self.question

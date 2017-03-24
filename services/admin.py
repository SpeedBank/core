from django.contrib import admin
from services.models import Faq, CustomerQuestion


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):

    list_display = ('bank', 'question')


@admin.register(CustomerQuestion)
class CustomerQuestionAdmin(admin.ModelAdmin):

    list_display = ('user', 'bank', 'question')

from django.contrib import admin

from .models import Inquiry, EventAdminInquiry

admin.site.register(Inquiry)
admin.site.register(EventAdminInquiry)
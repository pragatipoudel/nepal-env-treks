from django.contrib import admin

from .models import Activity, Season, Package

admin.site.register(Activity)
admin.site.register(Season)
admin.site.register(Package)
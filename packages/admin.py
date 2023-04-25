from django.contrib import admin

from .models import Activity, Season, Package, Amenity

admin.site.register(Activity)
admin.site.register(Season)
admin.site.register(Package)
admin.site.register(Amenity)
from django.contrib import admin

from .models import Activity, Season, Package, Amenity, DailyItinerary, FullItinerary


class DailyItineraryInline(admin.StackedInline):
    model = DailyItinerary


class FullItineraryAdmin(admin.ModelAdmin):
    inlines = [DailyItineraryInline]


admin.site.register(Activity)
admin.site.register(Season)
admin.site.register(Package)
admin.site.register(Amenity)
admin.site.register(FullItinerary, FullItineraryAdmin)
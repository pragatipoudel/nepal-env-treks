from django.contrib import admin

from .models import PriceTier, Activity, Season, Package, Amenity, DailyItinerary, FullItinerary, SpecialEvent


class DailyItineraryInline(admin.StackedInline):
    model = DailyItinerary


class FullItineraryAdmin(admin.ModelAdmin):
    inlines = [DailyItineraryInline]


class PriceTierInline(admin.TabularInline):
    model = PriceTier


class PackageAdmin(admin.ModelAdmin):
    inlines = [PriceTierInline]
    readonly_fields = ['slug']


admin.site.register(Activity)
admin.site.register(Season)
admin.site.register(SpecialEvent)
admin.site.register(Package, PackageAdmin)
admin.site.register(Amenity)
admin.site.register(FullItinerary, FullItineraryAdmin)
from django.contrib import admin
from .models import TimeSlots, TimeSlotRequest

class ReadOnlyFields(admin.ModelAdmin):
    readonly_fields = ('created_at',)

# Register your models here.
admin.site.register(TimeSlots)
admin.site.register(TimeSlotRequest, ReadOnlyFields)


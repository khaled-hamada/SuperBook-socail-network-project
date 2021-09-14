from django.contrib import admin
from .models import  Sighting, Location, Origin
# Register your models here.

class SightingAdmin(admin.ModelAdmin):
    list_display = ('superhero', 'power', 'location', 'sighted_on')
    date_hierarchy = 'sighted_on'
    search_fields = ('superhero',)
    ordering = ('superhero', )


admin.site.register(Sighting, SightingAdmin)
admin.site.register(Location)
admin.site.register(Origin)

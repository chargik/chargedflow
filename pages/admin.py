from django.contrib import admin
from .models import Tours


class ToursAdmin(admin.ModelAdmin):
    list_display = ('tour_name', 'timestamp', 'updated')


admin.site.register(Tours, ToursAdmin)

from django.contrib import admin
from .models import Join
# Register your models here.

class JoinAdmin(admin.ModelAdmin):
    list_display = ('lead_name', 'timestamp')

admin.site.register(Join, JoinAdmin)
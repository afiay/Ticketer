from __future__ import unicode_literals
 
from django.contrib import admin
 
class EventAdmin(admin.ModelAdmin):
    list_display = ['start_time', 'end_time', 'description']
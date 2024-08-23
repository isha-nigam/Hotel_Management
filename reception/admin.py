from django.contrib import admin
from . models import receptionist
from . models import guest_entries

# Register your models here.

admin.site.register(receptionist)
admin.site.register(guest_entries)
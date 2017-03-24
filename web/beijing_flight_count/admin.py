from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


admin.site.register(Ac_Number)
admin.site.register(Location)
admin.site.register(Check_Option)
admin.site.register(BeijingFlights)
admin.site.register(ActualTimetable)
admin.site.register(PlanTimetable)
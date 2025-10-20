from django.contrib import admin

# Register your models here.
from .models import Habit
admin.site.register(Habit)

from .models import Record
admin.site.register(Record)

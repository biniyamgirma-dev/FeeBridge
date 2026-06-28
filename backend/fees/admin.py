from django.contrib import admin
from .models import FeeStructure, Invoice

admin.site.register(FeeStructure)
admin.site.register(Invoice)
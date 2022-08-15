from django.contrib import admin
from .models import Phone


# Register your models here.
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass

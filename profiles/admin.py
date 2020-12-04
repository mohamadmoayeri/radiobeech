from django.contrib import admin

# Register your models here.

from .models import personal_information

from django.contrib.auth.models import Permission



admin.site.register(personal_information)
admin.site.register(Permission)



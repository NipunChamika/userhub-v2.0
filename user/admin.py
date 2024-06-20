from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    ordering = ['first_name', 'last_name', 'email']
    search_fields = ['first_name__istartswith',
                     'last_name__istartswith', 'email__istartswith']

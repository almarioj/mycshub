# -*- coding: utf-8 -*-
from django.contrib import admin

from accounts.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    # list_display = ('name', 'description', 'price')
    # search_fields = ('name',)
    # readonly_fields = list_display

admin.site.register(UserProfile, UserProfileAdmin)

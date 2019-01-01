# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Profile
from django.utils.html import format_html


class DocumentAdmin(admin.ModelAdmin):
    fields = ('user', 'create_date', 'update_date')
    # list_display = ('username', 'email', 'first_name', 'last_name', 'create_date', 'update_date')

    # def usage_link(self, obj):
    #     original_url = 'https://mindsapi.mindslab.ai/client/'
    #     return format_html('<a href="{}" target="_blank" >{}</a>', original_url+obj.clientID, obj.clientID)


admin.site.register(Profile, DocumentAdmin)

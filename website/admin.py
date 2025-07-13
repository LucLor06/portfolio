from django.contrib import admin
from .models import WebsiteContact, WebsiteSocial, WebsiteConfig
from solo.admin import SingletonModelAdmin

@admin.register(WebsiteContact)
class WebsiteContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'contact']


@admin.register(WebsiteSocial)
class WebsiteSocialAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(WebsiteConfig, SingletonModelAdmin)
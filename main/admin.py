from django.contrib import admin
from . import models

admin.site.register(models.Language)
admin.site.register(models.Technology)
admin.site.register(models.Tool)
admin.site.register(models.Skill)
admin.site.register(models.Tag)
from django.contrib import admin
from . import models


@admin.register(models.Code)
class CodeAdmin(admin.ModelAdmin):
    pass

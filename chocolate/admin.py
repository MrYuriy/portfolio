from django.contrib import admin
from .models import Project

class ProlectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)

admin.site.register(Project ,ProlectAdmin)
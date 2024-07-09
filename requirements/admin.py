from django.contrib import admin
from .models import Requirement, Document

class RequirementAdmin(admin.ModelAdmin):
    list_display=("title", "description", "created_at")

# Register your models here.
admin.site.register(Requirement, RequirementAdmin)
admin.site.register(Document)
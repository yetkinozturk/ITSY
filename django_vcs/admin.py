from django.contrib import admin

from django_vcs.models import CodeRepository

class CodeRepositoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }

admin.site.register(CodeRepository, CodeRepositoryAdmin)

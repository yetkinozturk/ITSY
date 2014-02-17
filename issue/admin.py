from django.contrib import admin
from issue import models


admin.site.register(models.IssueType)
admin.site.register(models.IssuePriority)
admin.site.register(models.IssueCharField)
admin.site.register(models.IssueTextField)
admin.site.register(models.IssueImageField)
admin.site.register(models.IssueFileField)
admin.site.register(models.IssuePerson)
admin.site.register(models.IssueStatus)
admin.site.register(models.IssueFlow)
admin.site.register(models.IssueTemplate)
admin.site.register(models.Issue)

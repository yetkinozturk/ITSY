from django.contrib import admin
from project import models


admin.site.register(models.MilestoneStatus)
admin.site.register(models.Milestone)
admin.site.register(models.ProjectCategory)
admin.site.register(models.ProjectVersion)
admin.site.register(models.Project)
admin.site.register(models.Board)

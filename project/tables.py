import django_tables2 as tables
from project import models as project_models


class MilestoneStatusTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/project/edit/milestatus/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/project/delete/milestatus/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = project_models.MilestoneStatus
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date')


class MilestoneTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/project/edit/milestone/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/project/delete/milestone/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = project_models.Milestone
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date','slug','effort_calc')


class ProjectCategoryTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/project/edit/category/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/project/delete/category/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = project_models.ProjectCategory
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date')


class ProjectTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/project/edit/project/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/project/delete/project/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = project_models.Project
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date','slug')


class ProjectVersionTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/project/edit/version/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/project/delete/version/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = project_models.ProjectVersion
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date')
import django_tables2 as tables
from issue import models as issue_models


class IssueTypeTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/issue/edit/type/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/issue/delete/type/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = issue_models.IssueType
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date')


class IssueStatusTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/issue/edit/status/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/issue/delete/status/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = issue_models.IssueStatus
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date')


class IssuePriorityTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/issue/edit/priority/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/issue/delete/priority/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = issue_models.IssuePriority
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date')


class IssueCharTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/issue/edit/char/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/issue/delete/char/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = issue_models.IssueCharField
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date')


class IssueBoolTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/issue/edit/bool/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/issue/delete/bool/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = issue_models.IssueBooleanField
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date')


class IssueDateTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/issue/edit/date/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/issue/delete/date/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = issue_models.IssueDatetimeField
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date')


class IssueChoiceTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/issue/edit/choice/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/issue/delete/choice/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = issue_models.IssueChoiceField
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date')


class IssueTextTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/issue/edit/text/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/issue/delete/text/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = issue_models.IssueTextField
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date')


class IssueImageTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/issue/edit/image/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/issue/delete/image/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = issue_models.IssueImageField
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date')


class IssueFileTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/issue/edit/file/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/issue/delete/file/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = issue_models.IssueFileField
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date')


class IssuePersonTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/issue/edit/person/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/issue/delete/person/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = issue_models.IssuePerson
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date')


class IssueFlowTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/issue/edit/flow/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/issue/delete/flow/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = issue_models.IssueFlow
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date')


class IssueTemplateTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/issue/edit/template/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/issue/delete/template/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = issue_models.IssueTemplate
        attrs = {"class": "paleblue"}
        exclude = ('id','entry_date')


class IssueTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/issue/view/details/{{record.slug}}/" style="color:red">View</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/issue/delete/item/{{record.id}}/" style="color:red">Delete</a>',orderable=False)

    class Meta:
        model = issue_models.Issue
        attrs = {"class": "paleblue"}
        exclude = (
            'template','slug','effort_calc','id','reporter','changelog',
            'summary')
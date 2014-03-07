import django_tables2 as tables
from repos.models import CodeRepository


class RepoTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/repos/edit/repos/{{record.id}}/" style="color:red">Edit</a>')
    delete_entries = tables.TemplateColumn('<a href="/repos/delete/repos/{{record.id}}/" style="color:red">Delete</a>')
    commits = tables.TemplateColumn('<a href="/repos/{{record.slug}}/" style="color:red">Recent Commits</a>')
    browse = tables.TemplateColumn('<a href="/repos/{{record.slug}}/browser/" style="color:red">Browse</a>')
    class Meta:
        model = CodeRepository
        attrs = {"class": "paleblue"}
        exclude = ('slug',)

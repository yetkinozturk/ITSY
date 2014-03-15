import django_tables2 as tables
from account.models import Account, AccountRole, AccountTeam


class AccountTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/account/edit/item/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/account/delete/item/{{record.id}}/" style="color:red">Delete</a>',orderable=False)
    class Meta:
        model = Account
        attrs = {"class": "paleblue"}
        exclude = ('slug','id','password')


class AccountRoleTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/account/edit/role/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/account/delete/role/{{record.id}}/" style="color:red">Delete</a>',orderable=False)
    class Meta:
        model = AccountRole
        attrs = {"class": "paleblue"}
        exclude = ('slug',)


class AccountTeamTable(tables.Table):
    edit_entries = tables.TemplateColumn('<a href="/account/edit/team/{{record.id}}/" style="color:red">Edit</a>',orderable=False)
    delete_entries = tables.TemplateColumn('<a href="/account/delete/team/{{record.id}}/" style="color:red">Delete</a>',orderable=False)
    class Meta:
        model = AccountTeam
        attrs = {"class": "paleblue"}
        exclude = ('slug',)

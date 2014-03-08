from django.conf.urls import patterns, url
from account.models import Account, AccountTeam, AccountRole
from account.views import CreateAccountItem, CreateAccountView

urlpatterns = patterns('',
    url(r'^item',
        CreateAccountView.as_view(
            model=Account,
            success_url='/account/view/item/',
            page_title = 'Create An Account',
            page_heading = 'Create An Account:',
        ),
        name='item'),

    url(r'^team',
        CreateAccountItem.as_view(
            model=AccountTeam,
            success_url='/account/view/team/',
            page_title = 'Create A Team',
            page_heading = 'Create A Team:',
        ),
        name='team'),

    url(r'^role',
        CreateAccountItem.as_view(
            model=AccountRole,
            success_url='/account/view/role/',
            page_title = 'Create A Role',
            page_heading = 'Create A Role:',
        ),
        name='role'),
)
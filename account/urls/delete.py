from django.conf.urls import patterns, url
from account.views import DeleteAccountItem
from account.models import Account, AccountRole, AccountTeam

urlpatterns = patterns('',

    url(r'^item/(?P<id>\w+)/',
        DeleteAccountItem.as_view(
            model=Account,
            success_url='/account/view/item/',
            page_title='ITSY Delete Account',
            page_heading='Delete Account:'
        ),
        name='item'),

    url(r'^role/(?P<id>\w+)/',
        DeleteAccountItem.as_view(
            model=AccountRole,
            success_url='/account/view/role/',
            page_title='ITSY Delete Account Role',
            page_heading='Delete Account Role:'
        ),
        name='role'),

    url(r'^team/(?P<id>\w+)/',
        DeleteAccountItem.as_view(
            model=AccountTeam,
            success_url='/account/view/team/',
            page_title='ITSY Delete Account Team',
            page_heading='Delete Account Team:'
        ),
        name='team'),
)
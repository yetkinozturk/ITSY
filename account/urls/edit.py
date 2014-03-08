from django.conf.urls import patterns, url
from account.views import UpdateAccountItem,UpdateAccount
from account.models import Account, AccountRole, AccountTeam

urlpatterns = patterns('',

    url(r'^item/(?P<id>\w+)/',
        UpdateAccount.as_view(
            model=Account,
            success_url='/account/view/item/',
            page_title='ITSY Edit Account',
            page_heading='Edit Account:',
            post_fix='item',
        ),
        name='item'),

    url(r'^role/(?P<id>\w+)/',
        UpdateAccountItem.as_view(
            model=AccountRole,
            success_url='/account/view/role/',
            page_title='ITSY Edit Account Role',
            page_heading='Edit Account Role:',
            post_fix='role',
        ),
        name='role'),

    url(r'^team/(?P<id>\w+)/',
        UpdateAccountItem.as_view(
            model=AccountTeam,
            success_url='/account/view/team/',
            page_title='ITSY Edit Account Team',
            page_heading='Edit Account Team:',
            post_fix='team',
        ),
        name='team'),
)
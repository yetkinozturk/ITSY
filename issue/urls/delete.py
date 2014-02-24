
from django.conf.urls import patterns, url
from issue.models import (IssueType, IssueStatus, IssuePriority,IssueCharField,
                          IssueTextField, IssueImageField,IssueFileField,
                          IssuePerson, IssueFlow, IssueTemplate, Issue,
                          IssueDatetimeField, IssueBooleanField,IssueChoiceField)
from issue.views import DeleteIssueItem


urlpatterns = patterns('',

    url(r'^type/(?P<id>\w+)/',
        DeleteIssueItem.as_view(
            model=IssueType,
            success_url='/issue/view/type/',
            page_title='ITSY Delete Issue Type',
            page_heading='Delete An Issue Type'
        ),
        name='type'),

    url(r'^status/(?P<id>\w+)/',
        DeleteIssueItem.as_view(
            model=IssueStatus,
            success_url='/issue/view/status/',
            page_title='ITSY Delete Issue Status',
            page_heading='Delete An Issue Status'
        ),
        name='status'),

    url(r'^priority/(?P<id>\w+)/',
        DeleteIssueItem.as_view(
            model=IssuePriority,
            success_url='/issue/view/priority/',
            page_title='ITSY Delete Issue Priority',
            page_heading='Delete An Issue Priority'
        ),
        name='priority'),

    url(r'^char/(?P<id>\w+)/',
        DeleteIssueItem.as_view(
            model=IssueCharField,
            success_url='/issue/view/char/',
            page_title='ITSY Delete Issue Text Field',
            page_heading='Delete An Issue Text Field'
        ),
        name='char'),

    url(r'^bool/(?P<id>\w+)/',
        DeleteIssueItem.as_view(
            model=IssueBooleanField,
            success_url='/issue/view/bool/',
            page_title='ITSY Delete Issue Boolean Field',
            page_heading='Delete An Issue Boolean Field'
        ),
        name='bool'),

    url(r'^date/(?P<id>\w+)/',
        DeleteIssueItem.as_view(
            model=IssueDatetimeField,
            success_url='/issue/view/date/',
            page_title='ITSY Delete Issue Datetime Field',
            page_heading='Delete An Issue Datetime Field'
        ),
        name='date'),

    url(r'^choice/(?P<id>\w+)/',
        DeleteIssueItem.as_view(
            model=IssueChoiceField,
            success_url='/issue/view/choice/',
            page_title='ITSY Delete Issue Choice Field',
            page_heading='Delete An Issue Choice Field'
        ),
        name='choice'),

    url(r'^text/(?P<id>\w+)/',
        DeleteIssueItem.as_view(
            model=IssueTextField,
            success_url='/issue/view/text/',
            page_title='ITSY Delete Issue Text Area Field',
            page_heading='Delete An Issue Text Area Field'
        ),
        name='text'),

    url(r'^image/(?P<id>\w+)/',
        DeleteIssueItem.as_view(
            model=IssueImageField,
            success_url='/issue/view/image/',
            page_title='ITSY Delete Issue Image Field',
            page_heading='Delete An Issue Image Field'
        ),
        name='image'),

    url(r'^file/(?P<id>\w+)/',
        DeleteIssueItem.as_view(
            model=IssueFileField,
            success_url='/issue/view/file/',
            page_title='ITSY Delete Issue File Field',
            page_heading='Delete An Issue File Field'
        ),
        name='file'),

    url(r'^person/(?P<id>\w+)/',
        DeleteIssueItem.as_view(
            model=IssuePerson,
            success_url='/issue/view/person/',
            page_title='ITSY Delete Issue Person Field',
            page_heading='Delete An Issue Person Field'
        ),name='person'),

    url(r'^flow/(?P<id>\w+)/',
        DeleteIssueItem.as_view(
            model=IssueFlow,
            success_url='/issue/view/flow/',
            page_title='ITSY Delete Issue Flow',
            page_heading='Delete An Issue Flow'
        ),
        name='flow'),

    url(r'^template/(?P<id>\w+)/',
        DeleteIssueItem.as_view(
            model=IssueTemplate,
            success_url='/issue/view/template/',
            page_title='ITSY Delete Issue Template',
            page_heading='Delete An Issue Template'
        ),
        name='template'),

    url(r'^item/(?P<id>\w+)/',
        DeleteIssueItem.as_view(
            model=Issue,
            page_title='ITSY Delete Issue',
            page_heading='Delete An Issue',
            success_url='/issue/view/item/',
        ),
        name='item'),
)
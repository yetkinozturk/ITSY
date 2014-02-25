from django.conf.urls import patterns, url
from issue.models import (IssueType, IssueStatus, IssuePriority,IssueCharField,
                          IssueTextField, IssueImageField,IssueFileField,
                          IssuePerson, IssueFlow, IssueTemplate, Issue,
                          IssueDatetimeField, IssueBooleanField,IssueChoiceField)
from issue.views import UpdateIssueField


urlpatterns = patterns('',

    url(r'^type/(?P<id>\w+)/',
        UpdateIssueField.as_view(
            model=IssueType,
            success_url='/issue/view/type/',
            page_title='ITSY Edit Issue Type',
            page_heading='Edit An Issue Type',
            post_fix='type',
        ),
        name='type'),

    url(r'^status/(?P<id>\w+)/',
        UpdateIssueField.as_view(
            model=IssueStatus,
            success_url='/issue/view/status/',
            page_title='ITSY Edit Issue Status',
            page_heading='Edit Issue Status:',
            post_fix='status',

        ),
        name='status'),

    url(r'^priority/(?P<id>\w+)/',
        UpdateIssueField.as_view(
            model=IssuePriority,
            success_url='/issue/view/priority/',
            page_title='ITSY Edit Issue Priority',
            page_heading='Edit Issue Priority:',
            post_fix='priority',
        ),
        name='priority'),

    url(r'^char/(?P<id>\w+)/',
        UpdateIssueField.as_view(
            model=IssueCharField,
            success_url='/issue/view/char/',
            page_title='ITSY Edit Issue Text Field',
            page_heading='Edit Issue Text Field:',
            post_fix='char',
        ),
        name='char'),

    url(r'^bool/(?P<id>\w+)/',
        UpdateIssueField.as_view(
            model=IssueBooleanField,
            success_url='/issue/view/bool/',
            page_title='ITSY Edit Issue Boolean Field',
            page_heading='Edit Issue Boolean Field:',
            post_fix='bool',
        ),
        name='bool'),

    url(r'^date/(?P<id>\w+)/',
        UpdateIssueField.as_view(
            model=IssueDatetimeField,
            success_url='/issue/view/date/',
            page_title='ITSY Edit Issue Datetime Field',
            page_heading='Edit Issue Datetime Field:',
            post_fix='date',
        ),
        name='date'),

    url(r'^choice/(?P<id>\w+)/',
        UpdateIssueField.as_view(
            model=IssueChoiceField,
            success_url='/issue/view/choice/',
            page_title='ITSY Edit Issue Choice Field',
            page_heading='Edit Issue Choice Field:',
            post_fix='choice',
        ),
        name='choice'),

    url(r'^text/(?P<id>\w+)/',
        UpdateIssueField.as_view(
            model=IssueTextField,
            success_url='/issue/view/text/',
            page_title='ITSY Edit Issue Text Area Field',
            page_heading='Edit Issue Text Area Field:',
            post_fix='text',
        ),
        name='text'),

    url(r'^image/(?P<id>\w+)/',
        UpdateIssueField.as_view(
            model=IssueImageField,
            success_url='/issue/view/image/',
            page_title='ITSY Edit Issue Image Field',
            page_heading='Edit Issue Image Field:',
            post_fix='image',
        ),
        name='image'),

    url(r'^file/(?P<id>\w+)/',
        UpdateIssueField.as_view(
            model=IssueFileField,
            success_url='/issue/view/file/',
            page_title='ITSY Edit Issue File Field',
            page_heading='Edit Issue File Field:',
            post_fix='file',
        ),
        name='file'),

    url(r'^person/(?P<id>\w+)/',
        UpdateIssueField.as_view(
            model=IssuePerson,
            success_url='/issue/view/person/',
            page_title='ITSY Edit Issue Person Field',
            page_heading='Edit Issue Person Field:',
            post_fix='person',
        ),name='person'),

    url(r'^flow/(?P<id>\w+)/',
        UpdateIssueField.as_view(
            model=IssueFlow,
            success_url='/issue/view/flow/',
            page_title='ITSY Edit Issue Flow',
            page_heading='Edit Issue Flow:',
            post_fix='flow',
        ),
        name='flow'),

    url(r'^template/(?P<id>\w+)/',
        UpdateIssueField.as_view(
            model=IssueTemplate,
            success_url='/issue/view/template/',
            page_title='ITSY Edit Issue Template',
            page_heading='Edit Issue Template:',
            post_fix='template',
        ),
        name='template'),
)
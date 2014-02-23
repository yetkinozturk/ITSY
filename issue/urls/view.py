from django.conf.urls import patterns, url
from issue.models import (IssueType, IssueStatus, IssuePriority,IssueCharField,
                          IssueTextField, IssueImageField,IssueFileField,
                          IssuePerson, IssueFlow, IssueTemplate, Issue,IssueTable)
from issue.views import (ListIssueFieldView, ListIssueView)


urlpatterns = patterns('',

    url(r'^type/',
        ListIssueFieldView.as_view(
            queryset=IssueType.objects.all(),
            context_object_name='object_list',
            page_title='ITSY Issue Types',
            page_heading='Issue Types:'
        ),
        name='type'),

    url(r'^status/',
        ListIssueFieldView.as_view(
            queryset=IssueStatus.objects.all(),
            context_object_name='object_list',
            page_title='ITSY Issue Statuses',
            page_heading='Issue Statuses:'
        ),
        name='status'),

    url(r'^priority/',
        ListIssueFieldView.as_view(
            queryset=IssuePriority.objects.all(),
            context_object_name='object_list',
            page_title='ITSY Issue Priorities',
            page_heading='Issue Priorities:'
        ),
        name='priority'),

    url(r'^char/',
        ListIssueFieldView.as_view(
            queryset=IssueCharField.objects.all(),
            context_object_name='object_list',
            page_title='ITSY Issue Text Fields',
            page_heading='Issue Text Fields:'
        ),
        name='char'),

    url(r'^text/',
        ListIssueFieldView.as_view(
            queryset=IssueTextField.objects.all(),
            context_object_name='object_list',
            page_title='ITSY Issue Text Area Fields',
            page_heading='Issue Text Area Fields:'
        ),
        name='text'),

    url(r'^image/',
        ListIssueFieldView.as_view(
            queryset=IssueImageField.objects.all(),
            context_object_name='object_list',
            page_title='ITSY Issue Image Fields',
            page_heading='Issue Image Fields:'
        ),
        name='image'),

    url(r'^file/',
        ListIssueFieldView.as_view(
            queryset=IssueFileField.objects.all(),
            context_object_name='object_list',
            page_title='ITSY Issue File Fields',
            page_heading='Issue File Fields:'
        ),
        name='file'),

    url(r'^person/',
        ListIssueFieldView.as_view(
            queryset=IssuePerson.objects.all(),
            context_object_name='object_list',
            page_title='ITSY Issue Person Fields',
            page_heading='Issue Person Fields:'
        ),name='person'),

    url(r'^flow/',
        ListIssueFieldView.as_view(
            queryset=IssueFlow.objects.all(),
            context_object_name='object_list',
            page_title='ITSY Issue Flows',
            page_heading='Issue Flows:'
        ),
        name='flow'),

    url(r'^template/',
        ListIssueFieldView.as_view(
            queryset=IssueTemplate.objects.all(),
            context_object_name='object_list',
            page_title='ITSY Issue Templates',
            page_heading='Issue Templates:'
        ),
        name='template'),

    url(r'^',
        ListIssueView.as_view(
            queryset=IssueTable(Issue.objects.all()),
            context_object_name='object_list',
        ),
        name='item'),
)
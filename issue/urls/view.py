from django.conf.urls import patterns, url
from issue.models import (IssueType, IssueStatus, IssuePriority,IssueCharField,
                          IssueTextField, IssueImageField,IssueFileField,
                          IssuePerson, IssueFlow, IssueTemplate, Issue,
                          IssueBooleanField, IssueDatetimeField, IssueChoiceField)
from issue.views import (ListIssueFieldView, ListIssueView)
from issue import tables as issue_tables


urlpatterns = patterns('',

    url(r'^type/',
        ListIssueFieldView.as_view(
            queryset=issue_tables.IssueTypeTable(IssueType.objects.all()),
            context_object_name='object_list',
            page_title='ITSY Issue Types',
            page_heading='Issue Types:'
        ),
        name='type'),

    url(r'^status/',
        ListIssueFieldView.as_view(
            queryset=issue_tables.IssueStatusTable(IssueStatus.objects.all()),
            context_object_name='object_list',
            page_title='ITSY Issue Statuses',
            page_heading='Issue Statuses:'
        ),
        name='status'),

    url(r'^priority/',
        ListIssueFieldView.as_view(
            queryset=issue_tables.IssuePriorityTable(IssuePriority.objects.all()),
            context_object_name='object_list',
            page_title='ITSY Issue Priorities',
            page_heading='Issue Priorities:'
        ),
        name='priority'),

    url(r'^char/',
        ListIssueFieldView.as_view(
            queryset=issue_tables.IssueCharTable(IssueCharField.objects.all()),
            context_object_name='object_list',
            page_title='ITSY Issue Text Fields',
            page_heading='Issue Text Fields:'
        ),
        name='char'),

    url(r'^bool/',
        ListIssueFieldView.as_view(
            queryset=issue_tables.IssueBoolTable(IssueBooleanField.objects.all()),
            context_object_name='object_list',
            page_title='ITSY Issue Boolean Fields',
            page_heading='Issue Boolean Fields:'
        ),
        name='bool'),

    url(r'^date/',
    ListIssueFieldView.as_view(
        queryset=issue_tables.IssueDateTable(IssueDatetimeField.objects.all()),
        context_object_name='object_list',
        page_title='ITSY Issue Datetime Fields',
        page_heading='Issue Datetime Fields:'
    ),
    name='date'),

    url(r'^choice/',
    ListIssueFieldView.as_view(
        queryset=issue_tables.IssueChoiceTable(IssueChoiceField.objects.all()),
        context_object_name='object_list',
        page_title='ITSY Issue Choice Fields',
        page_heading='Issue Choice Fields:'
    ),
    name='choice'),

    url(r'^text/',
        ListIssueFieldView.as_view(
            queryset=issue_tables.IssueTextTable(IssueTextField.objects.all()),
            context_object_name='object_list',
            page_title='ITSY Issue Text Area Fields',
            page_heading='Issue Text Area Fields:'
        ),
        name='text'),

    url(r'^image/',
        ListIssueFieldView.as_view(
            queryset=issue_tables.IssueImageTable(IssueImageField.objects.all()),
            context_object_name='object_list',
            page_title='ITSY Issue Image Fields',
            page_heading='Issue Image Fields:'
        ),
        name='image'),

    url(r'^file/',
        ListIssueFieldView.as_view(
            queryset=issue_tables.IssueFileTable(IssueFileField.objects.all()),
            context_object_name='object_list',
            page_title='ITSY Issue File Fields',
            page_heading='Issue File Fields:'
        ),
        name='file'),

    url(r'^person/',
        ListIssueFieldView.as_view(
            queryset=issue_tables.IssuePersonTable(IssuePerson.objects.all()),
            context_object_name='object_list',
            page_title='ITSY Issue Person Fields',
            page_heading='Issue Person Fields:'
        ),name='person'),

    url(r'^flow/',
        ListIssueFieldView.as_view(
            queryset=issue_tables.IssueFlowTable(IssueFlow.objects.all()),
            context_object_name='object_list',
            page_title='ITSY Issue Flows',
            page_heading='Issue Flows:'
        ),
        name='flow'),

    url(r'^template/',
        ListIssueFieldView.as_view(
            queryset=issue_tables.IssueTemplateTable(IssueTemplate.objects.all()),
            context_object_name='object_list',
            page_title='ITSY Issue Templates',
            page_heading='Issue Templates:'
        ),
        name='template'),

    url(r'^',
        ListIssueView.as_view(
            queryset=issue_tables.IssueTable(Issue.objects.all()),
            context_object_name='object_list',
        ),
        name='item'),
)
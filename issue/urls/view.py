from django.conf.urls import patterns, url
from issue.models import (IssueType, IssueStatus, IssuePriority,IssueCharField,
                          IssueTextField, IssueImageField,IssueFileField,
                          IssuePerson, IssueFlow, IssueTemplate, Issue,
                          IssueBooleanField, IssueDatetimeField, IssueChoiceField)
from issue.views import (ListIssueFieldView, ListIssueView,
                         ReadOnlyIssueDetailsView)
from issue import tables as issue_tables


urlpatterns = patterns('',

    url(r'^type/',
        ListIssueFieldView.as_view(
            queryset=IssueType.objects.all(),
            model=IssueType,
            table=issue_tables.IssueTypeTable,
            page_title='ITSY Issue Types',
            page_heading='Issue Types:'
        ),
        name='type'),

    url(r'^status/',
        ListIssueFieldView.as_view(
            queryset=IssueStatus.objects.all(),
            model=IssueStatus,
            table=issue_tables.IssueStatusTable,
            page_title='ITSY Issue Statuses',
            page_heading='Issue Statuses:'
        ),
        name='status'),

    url(r'^priority/',
        ListIssueFieldView.as_view(
            queryset=IssuePriority.objects.all(),
            table=issue_tables.IssuePriorityTable,
            model=IssuePriority,
            page_title='ITSY Issue Priorities',
            page_heading='Issue Priorities:'
        ),
        name='priority'),

    url(r'^char/',
        ListIssueFieldView.as_view(
            queryset=IssueCharField.objects.all(),
            table=issue_tables.IssueCharTable,
            model=IssueCharField,
            page_title='ITSY Issue Text Fields',
            page_heading='Issue Text Fields:'
        ),
        name='char'),

    url(r'^bool/',
        ListIssueFieldView.as_view(
            queryset=IssueBooleanField.objects.all(),
            table=issue_tables.IssueBoolTable,
            model=IssueBooleanField,
            page_title='ITSY Issue Boolean Fields',
            page_heading='Issue Boolean Fields:'
        ),
        name='bool'),

    url(r'^date/',
    ListIssueFieldView.as_view(
        queryset=IssueDatetimeField.objects.all(),
        table=issue_tables.IssueDateTable,
        model=IssueDatetimeField,
        page_title='ITSY Issue Datetime Fields',
        page_heading='Issue Datetime Fields:'
    ),
    name='date'),

    url(r'^choice/',
    ListIssueFieldView.as_view(
        queryset=IssueChoiceField.objects.all(),
        table=issue_tables.IssueChoiceTable,
        model=IssueChoiceField,
        page_title='ITSY Issue Choice Fields',
        page_heading='Issue Choice Fields:'
    ),
    name='choice'),

    url(r'^text/',
        ListIssueFieldView.as_view(
            queryset=IssueTextField.objects.all(),
            table=issue_tables.IssueTextTable,
            model=IssueTextField,
            page_title='ITSY Issue Text Area Fields',
            page_heading='Issue Text Area Fields:'
        ),
        name='text'),

    url(r'^image/',
        ListIssueFieldView.as_view(
            queryset=IssueImageField.objects.all(),
            table=issue_tables.IssueImageTable,
            model=IssueImageField,
            page_title='ITSY Issue Image Fields',
            page_heading='Issue Image Fields:'
        ),
        name='image'),

    url(r'^file/',
        ListIssueFieldView.as_view(
            queryset=IssueFileField.objects.all(),
            table=issue_tables.IssueFileTable,
            model=IssueFileField,
            page_title='ITSY Issue File Fields',
            page_heading='Issue File Fields:'
        ),
        name='file'),

    url(r'^person/',
        ListIssueFieldView.as_view(
            queryset=IssuePerson.objects.all(),
            table=issue_tables.IssuePersonTable,
            model=IssuePerson,
            page_title='ITSY Issue Person Fields',
            page_heading='Issue Person Fields:'
        ),name='person'),

    url(r'^flow/',
        ListIssueFieldView.as_view(
            queryset=IssueFlow.objects.all(),
            table=issue_tables.IssueFlowTable,
            model=IssueFlow,
            page_title='ITSY Issue Flows',
            page_heading='Issue Flows:'
        ),
        name='flow'),

    url(r'^template/',
        ListIssueFieldView.as_view(
            queryset=IssueTemplate.objects.all(),
            table=issue_tables.IssueTemplateTable,
            model=IssueTemplate,
            page_title='ITSY Issue Templates',
            page_heading='Issue Templates:'
        ),
        name='template'),

    url(r'^details/(?P<slug>\w+)/',
        ReadOnlyIssueDetailsView.as_view(
            model=Issue,
            success_url='/issue/view/item/',
            template_name = 'issue/view/issuedetails.html'
        ),
        name='details'),

    url(r'^',
        ListIssueView.as_view(
            queryset=Issue.objects.all(),
            table=issue_tables.IssueTable,
            model=Issue,
        ),
        name='item'),
)
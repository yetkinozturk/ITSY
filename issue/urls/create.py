from django.conf.urls import patterns, url
from issue.models import (IssueType, IssueStatus, IssuePriority,IssueCharField,
                          IssueTextField, IssueImageField,IssueFileField,
                          IssuePerson, IssueFlow, IssueTemplate, Issue,
                          IssueDatetimeField, IssueBooleanField,IssueChoiceField)
from issue.views import (CreateIssueView, CreateIssueFlow, CreateIssueField,
                         CreateIssueDetails)


urlpatterns = patterns('',

    url(r'^type/',
        CreateIssueField.as_view(
            model=IssueType,
            success_url='/issue/view/type/',
            page_title='ITSY Create Issue Type',
            page_heading='Create An Issue Type'
        ),
        name='type'),

    url(r'^status/',
        CreateIssueField.as_view(
            model=IssueStatus,
            success_url='/issue/view/status/',
            page_title='ITSY Create Issue Status',
            page_heading='Create An Issue Status'
        ),
        name='status'),

    url(r'^priority/',
        CreateIssueField.as_view(
            model=IssuePriority,
            success_url='/issue/view/priority/',
            page_title='ITSY Create Issue Priority',
            page_heading='Create An Issue Priority'
        ),
        name='priority'),

    url(r'^char/',
        CreateIssueField.as_view(
            model=IssueCharField,
            success_url='/issue/view/char/',
            page_title='ITSY Create Issue Text Field',
            page_heading='Create An Issue Text Field'
        ),
        name='char'),

    url(r'^bool/',
        CreateIssueField.as_view(
            model=IssueBooleanField,
            success_url='/issue/view/bool/',
            page_title='ITSY Create Issue Boolean Field',
            page_heading='Create An Issue Boolean Field'
        ),
        name='bool'),

    url(r'^date/',
        CreateIssueField.as_view(
            model=IssueDatetimeField,
            success_url='/issue/view/date/',
            page_title='ITSY Create Issue Datetime Field',
            page_heading='Create An Issue Datetime Field'
        ),
        name='date'),

    url(r'^choice/',
        CreateIssueField.as_view(
            model=IssueChoiceField,
            success_url='/issue/view/choice/',
            page_title='ITSY Create Issue Choice Field',
            page_heading='Create An Issue Choice Field'
        ),
        name='choice'),

    url(r'^text/',
        CreateIssueField.as_view(
            model=IssueTextField,
            success_url='/issue/view/text/',
            page_title='ITSY Create Issue Text Area Field',
            page_heading='Create An Issue Text Area Field'
        ),
        name='text'),

    url(r'^image/',
        CreateIssueField.as_view(
            model=IssueImageField,
            success_url='/issue/view/image/',
            page_title='ITSY Create Issue Image Field',
            page_heading='Create An Issue Image Field'
        ),
        name='image'),

    url(r'^file/',
        CreateIssueField.as_view(
            model=IssueFileField,
            success_url='/issue/view/file/',
            page_title='ITSY Create Issue File Field',
            page_heading='Create An Issue File Field'
        ),
        name='file'),

    url(r'^person/',
        CreateIssueField.as_view(
            model=IssuePerson,
            success_url='/issue/view/person/',
            page_title='ITSY Create Issue Person Field',
            page_heading='Create An Issue Person Field'
        ),name='person'),

    url(r'^flow/',
        CreateIssueFlow.as_view(
            model=IssueFlow,
            success_url='/issue/view/flow/',
            template_name = 'issue/create/issueflow.html'
        ),
        name='flow'),

    url(r'^template/',
        CreateIssueField.as_view(
            model=IssueTemplate,
            success_url='/issue/view/template/',
            fields = [
                'name','char_fields','text_fields','bool_fields','date_fields',
                'choice_fields','image_fields','file_fields',
                'people','project',
            ],
            page_title='ITSY Create Issue Template',
            page_heading='Create An Issue Template'
        ),
        name='template'),

    url(r'^details/(?P<slug>\w+)/',
        CreateIssueDetails.as_view(
            model=Issue,
            success_url='/issue/view/item/',
            template_name = 'issue/create/issuedetails.html'
        ),
        name='details'),

    url(r'^',
        CreateIssueView.as_view(
            model=Issue,
            success_url='/issue/create/details/',
            fields = [
                'title', 'summary', 'effort', 'project_version', 'type',
                'status', 'priority', 'template', 'sub_issues','due_date'
            ],
            template_name = 'issue/create/issue.html'
        ),
        name='item'),
)
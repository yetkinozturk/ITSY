from django.conf.urls import patterns, url
from issue.models import (IssueType, IssueStatus, IssuePriority,IssueCharField,
                          IssueTextField, IssueImageField,IssueFileField,
                          IssuePerson, IssueFlow, IssueTemplate, Issue)
from issue.views import (CreateIssueView, CreateIssueFlow, CreateIssueField)


urlpatterns = patterns('',

    url(r'^type/',
        CreateIssueField.as_view(
            model=IssueType,
            page_title='ITSY Create Issue Type',
            page_heading='Create An Issue Type'
        ),
        name='type'),

    url(r'^status/',
        CreateIssueField.as_view(
            model=IssueStatus,
            page_title='ITSY Create Issue Status',
            page_heading='Create An Issue Status'
        ),
        name='status'),

    url(r'^priority/',
        CreateIssueField.as_view(
            model=IssuePriority,
            page_title='ITSY Create Issue Priority',
            page_heading='Create An Issue Priority'
        ),
        name='priority'),

    url(r'^char/',
        CreateIssueField.as_view(
            model=IssueCharField,
            page_title='ITSY Create Issue Text Field',
            page_heading='Create An Issue Text Field'
        ),
        name='char'),

    url(r'^text/',
        CreateIssueField.as_view(
            model=IssueTextField,
            page_title='ITSY Create Issue Text Area Field',
            page_heading='Create An Issue Text Area Field'
        ),
        name='text'),

    url(r'^image/',
        CreateIssueField.as_view(
            model=IssueImageField,
            page_title='ITSY Create Issue Image Field',
            page_heading='Create An Issue Image Field'
        ),
        name='image'),

    url(r'^file/',
        CreateIssueField.as_view(
            model=IssueFileField,
            page_title='ITSY Create Issue File Field',
            page_heading='Create An Issue File Field'
        ),
        name='file'),

    url(r'^person/',
        CreateIssueField.as_view(
            model=IssuePerson,
            page_title='ITSY Create Issue Person Field',
            page_heading='Create An Issue Person Field'
        ),name='person'),

    url(r'^flow/',
        CreateIssueFlow.as_view(
            model=IssueFlow,
            template_name = 'issue/create/issueflow.html'
        ),
        name='flow'),

    url(r'^template/',
        CreateIssueField.as_view(
            model=IssueTemplate,
            fields = [
                'name','char_fields','text_fields','image_fields','file_fields',
                'people','project',
            ],
            page_title='ITSY Create Issue Template',
            page_heading='Create An Issue Template'
        ),
        name='template'),

    url(r'^',
        CreateIssueView.as_view(
            model=Issue,
            fields = [
                'title', 'summary', 'effort', 'project_version', 'type',
                'status', 'priority', 'template', 'flow', 'sub_issues','due_date'
            ],
            template_name = 'issue/create/issue.html'
        ),
        name='item'),
)
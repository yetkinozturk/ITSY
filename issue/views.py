from django.core.context_processors import csrf
from django.shortcuts import render
from django.views.generic.base import View
from django.forms import ModelForm
from issue.models import (Issue, IssueType)


class CreateIssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = [
            'title', 'summary', 'effort', 'project_version', 'type',
            'status', 'priority', 'template', 'flow', 'sub_issues','due_date'
        ]


class CreateIssueView(View):
    template_name = 'issue/createissue.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_form'] = CreateIssueForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        return render(request, self.template_name)


class CreateIssueTypeForm(ModelForm):
    class Meta:
        model = IssueType
        fields = [
            'name',
        ]


class CreateIssueTypeView(View):
    template_name = 'issue/createissuetype.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_type_form'] = CreateIssueTypeForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        return render(request, self.template_name)
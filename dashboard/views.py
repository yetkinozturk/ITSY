from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.forms import ModelForm
from issue.models import Issue


class CreateIssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = [
            'title', 'summary', 'effort', 'project_version', 'type',
            'status', 'priority', 'template', 'flow', 'sub_issues','due_date'
        ]


class MainDashboardView(View):
    template_name = 'dashboard/main.html'

    def get(self,request):
        content = {}
        content['create_issue_form'] = CreateIssueForm()
        return render(request, self.template_name, content)

    def post(self,request):
        return render(request, self.template_name)

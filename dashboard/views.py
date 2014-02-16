from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from issue.models import (IssueType, IssueStatus, IssueFlow, IssuePriority,
                          IssueTemplate)
from project.models import ProjectVersion

class MainDashboardView(View):
    template_name = 'dashboard/main.html'

    def get(self,request):
        content = {}
        content['issue_type_list'] = IssueType.objects.all()
        content['issue_status_list'] = IssueStatus.objects.all()
        content['issue_priority_list'] = IssuePriority.objects.all()
        content['issue_template_list'] = IssueTemplate.objects.all()
        content['issue_flow_list'] = IssueFlow.objects.all()
        content['project_version_list'] = ProjectVersion.objects.all()
        return render(request, self.template_name, content)

    def post(self,request):
        return render(request, self.template_name)

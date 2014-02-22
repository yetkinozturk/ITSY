from django.conf.urls import patterns, url
from django.views.generic import ListView
from project.models import (Project,ProjectCategory,ProjectVersion,Milestone,
                            MilestoneStatus)

urlpatterns = patterns('',

    url(r'^project/',
        ListView.as_view(
            queryset=Project.objects.all(),
            context_object_name='project_list',
            template_name='project/view/project.html'
        ),
        name='project'),

    url(r'^category/',
        ListView.as_view(
            queryset=ProjectCategory.objects.all(),
            context_object_name='project_category_list',
            template_name='project/view/category.html'
        ),
        name='category'),

    url(r'^version/',
        ListView.as_view(
            queryset=ProjectVersion.objects.all(),
            context_object_name='project_version_list',
            template_name='project/view/version.html'
        ),
        name='version'),

    url(r'^milestone/',
        ListView.as_view(
            queryset=Milestone.objects.all(),
            context_object_name='milestone_list',
            template_name='project/view/milestone.html'
        ),
        name='milestone'),

    url(r'^milestatus/',
        ListView.as_view(
            queryset=MilestoneStatus.objects.all(),
            context_object_name='milestone_status_list',
            template_name='project/view/milestatus.html'
        ),    name='milestatus'),
)


from django.conf.urls import patterns, url
from project.views import ListProjectView
from project.models import (Project,ProjectCategory,ProjectVersion,Milestone,
                            MilestoneStatus)

urlpatterns = patterns('',

    url(r'^project/',
        ListProjectView.as_view(
            queryset=Project.objects.all(),
            context_object_name='object_list',
            page_title='ITSY Issue Projects',
            page_heading='Projects:'
        ),
        name='project'),

    url(r'^category/',
        ListProjectView.as_view(
            queryset=ProjectCategory.objects.all(),
            context_object_name='object_list',
            page_title='ITSY Project Categories',
            page_heading='Project Categories:'
        ),
        name='category'),

    url(r'^version/',
        ListProjectView.as_view(
            queryset=ProjectVersion.objects.all(),
            context_object_name='object_list',
            page_title='ITSY Project Versions',
            page_heading='Project Versions:'
        ),
        name='version'),

    url(r'^milestone/',
        ListProjectView.as_view(
            queryset=Milestone.objects.all(),
            context_object_name='object_list',
            page_title='ITSY Milestones',
            page_heading='Milestones:'
        ),
        name='milestone'),

    url(r'^milestatus/',
        ListProjectView.as_view(
            queryset=MilestoneStatus.objects.all(),
            context_object_name='object_list',
            page_title='ITSY Milestone Statuses',
            page_heading='Milestone Statuses:'
        ),    name='milestatus'),
)


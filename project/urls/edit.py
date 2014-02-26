from django.conf.urls import patterns, url
from project.views import UpdateProjectItem
from project.models import (Project,ProjectCategory,ProjectVersion,Milestone,
                            MilestoneStatus)

urlpatterns = patterns('',

    url(r'^project/(?P<id>\w+)/',
        UpdateProjectItem.as_view(
            model=Project,
            success_url='/project/view/project/',
            page_title='ITSY Edit Issue Project',
            page_heading='Edit Project:'
        ),
        name='project'),

    url(r'^category/(?P<id>\w+)/',
        UpdateProjectItem.as_view(
            model=ProjectCategory,
            success_url='/project/view/category/',
            page_title='ITSY Edit Project Category',
            page_heading='Edit Project Category:'
        ),
        name='category'),

    url(r'^version/(?P<id>\w+)/',
        UpdateProjectItem.as_view(
            model=ProjectVersion,
            success_url='/project/view/version/',
            page_title='ITSY Edit Project Version',
            page_heading='Edit Project Version:'
        ),
        name='version'),

    url(r'^milestone/(?P<id>\w+)/',
        UpdateProjectItem.as_view(
            model=Milestone,
            success_url='/project/view/milestone/',
            page_title='ITSY Edit Milestone',
            page_heading='Edit Milestone:'
        ),
        name='milestone'),

    url(r'^milestatus/(?P<id>\w+)/',
        UpdateProjectItem.as_view(
            model=MilestoneStatus,
            success_url='/project/view/milestatus/',
            page_title='ITSY Edit Milestone Status',
            page_heading='Edit Milestone Status:'
        ),    name='milestatus'),
)




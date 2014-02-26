from django.conf.urls import patterns, url
from project.views import DeleteProjectItem
from project.models import (Project,ProjectCategory,ProjectVersion,Milestone,
                            MilestoneStatus)

urlpatterns = patterns('',

    url(r'^project/(?P<id>\w+)/',
        DeleteProjectItem.as_view(
            model=Project,
            success_url='/project/view/project/',
            page_title='ITSY Delete Issue Project',
            page_heading='Delete Project:'
        ),
        name='project'),

    url(r'^category/(?P<id>\w+)/',
        DeleteProjectItem.as_view(
            model=ProjectCategory,
            success_url='/project/view/category/',
            page_title='ITSY Delete Project Category',
            page_heading='Delete Project Category:'
        ),
        name='category'),

    url(r'^version/(?P<id>\w+)/',
        DeleteProjectItem.as_view(
            model=ProjectVersion,
            success_url='/project/view/version/',
            page_title='ITSY Delete Project Version',
            page_heading='Delete Project Version:'
        ),
        name='version'),

    url(r'^milestone/(?P<id>\w+)/',
        DeleteProjectItem.as_view(
            model=Milestone,
            success_url='/project/view/milestone/',
            page_title='ITSY Delete Milestone',
            page_heading='Delete Milestone:'
        ),
        name='milestone'),

    url(r'^milestatus/(?P<id>\w+)/',
        DeleteProjectItem.as_view(
            model=MilestoneStatus,
            success_url='/project/view/milestatus/',
            page_title='ITSY Delete Milestone Status',
            page_heading='Delete Milestone Status:'
        ),    name='milestatus'),
)




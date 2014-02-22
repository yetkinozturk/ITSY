from django.conf.urls import patterns, url
from django.views.generic.edit import CreateView
from project.models import (Project,ProjectCategory,ProjectVersion,Milestone,
                            MilestoneStatus)

urlpatterns = patterns('',

    url(r'^project/',
        CreateView.as_view(
            model=Project,
            template_name='project/create/project.html',
            success_url='/project/view/project/'
        ),
        name='project'),

    url(r'^category/',
        CreateView.as_view(
            model=ProjectCategory,
            template_name='project/create/category.html',
            success_url='/project/view/category/'
        ),
        name='category'),

    url(r'^version/',
        CreateView.as_view(
            model=ProjectVersion,
            template_name='project/create/version.html',
            success_url='/project/view/version/'
        ),
        name='version'),

    url(r'^milestone/',
        CreateView.as_view(
            model=Milestone,
            template_name='project/create/milestone.html',
            success_url='/project/view/milestone/'
        ),
        name='milestone'),

    url(r'^milestatus/',
        CreateView.as_view(
            model=MilestoneStatus,
            template_name='project/create/milestatus.html',
            success_url='/project/view/milestatus/'
        ),    name='milestatus'),
)
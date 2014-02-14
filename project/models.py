from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import Account


class MilestoneStatus(models.Model):
    status = models.CharField(_(u'Status'), max_length=128)


class Milestone(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)
    effort = models.CharField(_(u'Effort'),max_length=128, null=True, blank=True)
    effort_calc = models.PositiveIntegerField(_(u'Effort Calculated'), null=True, blank=True)
    responsible = models.ForeignKey(Account, verbose_name=_(u'Responsible'), null=True, blank=True)
    status = models.ForeignKey(MilestoneStatus,verbose_name=_(u'Status'), null=True, blank=True)
    due_date = models.DateTimeField(_(u'Due Date'), null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)


class ProjectCategory(models.Model):
    name = models.CharField(_(u'Category Name'), max_length=128)
    responsible = models.ForeignKey(Account, verbose_name=_(u'Responsible'), null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)


class ProjectVersion(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)
    summary = models.TextField(_(u'Summary'), null=True, blank=True)
    milestones = models.ManyToManyField(Milestone, verbose_name=_(u'Milestones'))
    category = models.ForeignKey(ProjectCategory, verbose_name=_(u'Category'))
    responsible = models.ForeignKey(Account, verbose_name=_(u'Responsible'), null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)


class Project(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)
    summary = models.TextField(_(u'Summary'), null=True, blank=True)
    versions = models.ManyToManyField(ProjectVersion, verbose_name=_(u'Versions'))
    responsible = models.ForeignKey(Account, verbose_name=_(u'Responsible'), null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)


class Board(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)
    summary = models.TextField(_(u'Summary'), null=True, blank=True)
    project = models.ForeignKey(Project, _(u'Project'))
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)
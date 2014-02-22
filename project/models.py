from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import Account
from autoslug import AutoSlugField

class MilestoneStatus(models.Model):
    status = models.CharField(_(u'Status'), max_length=128)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)

    class Meta:
        ordering = ['-entry_date']

    def __unicode__(self):
        return self.status


class Milestone(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    effort = models.CharField(_(u'Effort'),max_length=128, null=True, blank=True)
    effort_calc = models.PositiveIntegerField(_(u'Effort Calculated'), null=True, blank=True)
    bug_to_fixed = models.PositiveIntegerField(_(u'Bugs to Fixed'), null=True, blank=True)
    bug_fixed = models.PositiveIntegerField(_(u'Bugs Fixed'), null=True, blank=True)
    feature_to_develop = models.PositiveIntegerField(_(u'Feature to Develop'), null=True, blank=True)
    feature_developed = models.PositiveIntegerField(_(u'Feature Developed'), null=True, blank=True)
    responsible = models.ForeignKey(Account, verbose_name=_(u'Responsible'), null=True, blank=True)
    status = models.ForeignKey(MilestoneStatus,verbose_name=_(u'Status'), null=True, blank=True)
    due_date = models.DateTimeField(_(u'Due Date'), null=True, blank=True)
    complete_date = models.DateTimeField(_(u'Date Completed'), null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)

    class Meta:
        ordering = ['-entry_date']

    def __unicode__(self):
        return self.title


class ProjectCategory(models.Model):
    name = models.CharField(_(u'Category Name'), max_length=128)
    responsible = models.ForeignKey(Account, verbose_name=_(u'Responsible'), null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)

    class Meta:
        ordering = ['-entry_date']

    def __unicode__(self):
        return self.name


class ProjectVersion(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)
    summary = models.TextField(_(u'Summary'), null=True, blank=True)
    milestones = models.ManyToManyField(Milestone, verbose_name=_(u'Milestones'))
    category = models.ForeignKey(ProjectCategory, verbose_name=_(u'Category'))
    responsible = models.ForeignKey(Account, verbose_name=_(u'Responsible'), null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)

    class Meta:
        ordering = ['-entry_date']

    def __unicode__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    summary = models.TextField(_(u'Summary'), null=True, blank=True)
    versions = models.ManyToManyField(ProjectVersion, verbose_name=_(u'Versions'),null=True,blank=True)
    responsible = models.ForeignKey(Account, verbose_name=_(u'Responsible'), null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)

    class Meta:
        ordering = ['-entry_date']

    def __unicode__(self):
        return self.title


class ProjectMembership(models.Model):
    project = models.ForeignKey(Project, verbose_name=_(u'Project'))
    members = models.ManyToManyField(Account,verbose_name=_(u'Members'),null=True,blank=True)


class Board(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    summary = models.TextField(_(u'Summary'), null=True, blank=True)
    project = models.ForeignKey(Project, verbose_name=_(u'Project'))
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)

    class Meta:
        ordering = ['-entry_date']

    def __unicode__(self):
        return self.title
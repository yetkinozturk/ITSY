import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import Account
from common.models import Comment
from common.fields import ListField
from project.models import ProjectVersion, Project
from autoslug import AutoSlugField
from taggit.managers import TaggableManager

class IssueType(models.Model):
    name = models.CharField(_(u'Type Name'), max_length=128)

    def __unicode__(self):
        return self.name


class IssuePriority(models.Model):
    name = models.CharField(_(u'Issue Priority'), max_length=128)

    def __unicode__(self):
        return self.name


class IssueCharField(models.Model):
    name = models.CharField(_(u'Field Name'), max_length=128)
    value = models.CharField(_(u'Field Value'), max_length=255,null=True,blank=True)

    def __unicode__(self):
        return self.name


class IssueTextField(models.Model):
    name = models.CharField(_(u'Field Name'), max_length=128)
    value = models.TextField(_(u'Field Value'), null=True,blank=True)

    def __unicode__(self):
        return self.name


class IssueImageField(models.Model):
    name = models.CharField(_(u'Field Name'), max_length=128)
    value = models.ImageField(_(u'Image'), upload_to='Issue Images', null=True, blank=True)

    def __unicode__(self):
        return self.name

class IssueFileField(models.Model):
    name = models.CharField(_(u'Field Name'), max_length=128)
    value = models.ImageField(_(u'File'), upload_to='Issue Files', null=True, blank=True)

    def __unicode__(self):
        return self.name


class IssuePerson(models.Model):
    role = models.CharField(_(u'Role Name'), max_length=128)
    account_id = models.PositiveIntegerField(_(u'Account ID'),null=True,blank=True)

    def __unicode__(self):
        return self.role


class IssueStatus(models.Model):
    status = models.CharField(_(u'Status'), max_length=128)

    def __unicode__(self):
        return self.status


class IssueFlow(models.Model):
    name = models.CharField(_(u'Flow Name'), max_length=128)
    accounts = ListField(_(u'Accounts List'), null=True, blank=True)
    current = models.PositiveIntegerField(_(u'Current'), null=True, blank=True)
    next = models.PositiveIntegerField(_(u'Next'), null=True, blank=True)
    prev = models.PositiveIntegerField(_(u'Previous'), null=True, blank=True)

    def __unicode__(self):
        return self.name


class IssueTemplate(models.Model):
    name = models.CharField(_(u'Template Name'), max_length=128)
    char_fields = models.ManyToManyField(IssueCharField, verbose_name=_(u'Char Fields'), null=True, blank=True)
    text_fields = models.ManyToManyField(IssueTextField, verbose_name=_(u'Text Fields'), null=True, blank=True)
    image_fields = models.ManyToManyField(IssueImageField, verbose_name=_(u'Image Fields'), null=True, blank=True)
    file_fields = models.ManyToManyField(IssueFileField, verbose_name=_(u'File Fields'),null=True, blank=True)
    people = models.ManyToManyField(IssuePerson, verbose_name=_(u'People'), null=True, blank=True )
    project = models.ForeignKey(Project,verbose_name=_(u'Project'), null=True, blank=True)

    def __unicode__(self):
        return self.name


class Issue(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    summary = models.TextField(_(u'Summary'), null=True, blank=True)
    effort = models.CharField(_(u'Effort'),max_length=128, null=True, blank=True)
    effort_calc = models.PositiveIntegerField(_(u'Effort Calculated'), null=True, blank=True)
    project_version = models.ForeignKey(ProjectVersion,verbose_name=_(u'Project Version'), blank=True,null=True)
    reporter = models.ForeignKey(Account, verbose_name=_(u'Assignee'), null=True, blank=True)

    type = models.ForeignKey(IssueType, verbose_name=_(u'Type'), null=True, blank=True)
    status = models.ForeignKey(IssueStatus,verbose_name=_(u'Status'), null=True, blank=True)
    priority = models.ForeignKey(IssuePriority, verbose_name=_(u'Priority'), null=True, blank=True)
    tags = TaggableManager(blank=True)
    template = models.ForeignKey(IssueTemplate, verbose_name=_(u'Issue Template'), null=True, blank=True)
    flow = models.ForeignKey(IssueFlow, verbose_name=_(u'Issue Flow'), null=True,blank=True)
    sub_issues = models.ManyToManyField('self', null=True, blank=True)

    is_draft = models.BooleanField(_(u'Draft'), default=True)
    end_date =  models.DateTimeField(_(u'End Date'), null=True, blank=True)
    due_date = models.DateTimeField(_(u'Due Date'), null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)

    def __unicode__(self):
        return self.title

    def overdue_status(self):
        if datetime.date.today() > self.due_date :
            return True
        else:
            return False


class IssueWatch(models.Model):
    issue = models.ForeignKey(Issue, verbose_name=_(u'Issue'))
    watchers = models.ManyToManyField(Account, verbose_name=_(u'Watchers'))


class IssueComment(models.Model):
    models.ForeignKey(Issue, verbose_name=_(u'Issue'))
    models.ManyToManyField(Comment, verbose_name=_(u'Comments'))
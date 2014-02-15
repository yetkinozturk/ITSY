from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import Account
from common.models import Comment
from project.models import ProjectVersion


class IssueType(models.Model):
    name = models.CharField(_(u'Type Name'), max_length=128)


class IssuePriority(models.Model):
    name = models.CharField(_(u'Issue Priority'), max_length=128)


class IssueCharField(models.Model):
    name = models.CharField(_(u'Field Name'), max_length=128)
    value = models.CharField(_(u'Field Value'), max_length=255,null=True,blank=True)


class IssueTextField(models.Model):
    name = models.CharField(_(u'Field Name'), max_length=128)
    value = models.TextField(_(u'Field Value'), null=True,blank=True)


class IssueImageField(models.Model):
    name = models.CharField(_(u'Field Name'), max_length=128)
    value = models.ImageField(_(u'Image'), upload_to='Issue Images', null=True, blank=True)


class IssuePerson(models.Model):
    role = models.CharField(_(u'Role Name'), max_length=128)
    person = models.ForeignKey(Account, verbose_name=_(u'Person'), null=True, blank=True)


class IssueStatus(models.Model):
    status = models.CharField(_(u'Status'), max_length=128)


#todo
class IssueFlow(models.Model):
    pass


class Issue(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)
    summary = models.TextField(_(u'Summary'), null=True, blank=True)
    effort = models.CharField(_(u'Effort'),max_length=128, null=True, blank=True)
    effort_calc = models.PositiveIntegerField(_(u'Effort Calculated'), null=True, blank=True)

    type = models.ForeignKey(IssueType, verbose_name=_(u'Type'), null=True, blank=True)
    status = models.ForeignKey(IssueStatus,verbose_name=_(u'Status'), null=True, blank=True)
    project_version = models.ForeignKey(ProjectVersion,verbose_name=_(u'Project Version'), blank=True,null=True)
    priority = models.ForeignKey(IssuePriority, verbose_name=_(u'Priority'), null=True, blank=True)
    assignee = models.ForeignKey(Account, verbose_name=_(u'Assignee'), null=True, blank=True)
    holder = models.ForeignKey(Account, verbose_name=_(u'Current Holder'),null=True,blank=True)
    char_fields = models.ManyToManyField(IssueCharField, verbose_name=_(u'Char Fields'), null=True, blank=True)
    text_fields = models.ManyToManyField(IssueTextField, verbose_name=_(u'Text Fields'), null=True, blank=True)
    image_fields = models.ManyToManyField(IssueImageField, verbose_name=_(u'Image Fields'), null=True, blank=True)
    people = models.ManyToManyField(IssuePerson, verbose_name=_(u'People'), null=True, blank=True )
    sub_issues = models.ManyToManyField('self', null=True, blank=True)

    end_date =  models.DateTimeField(_(u'End Date'), null=True, blank=True)
    due_date = models.DateTimeField(_(u'Due Date'), null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)


class IssueWatch(models.Model):
    issue = models.ForeignKey(Issue, verbose_name=_(u'Issue'))
    watchers = models.ManyToManyField(Account, verbose_name=_(u'Watchers'))


class IssueComment(models.Model):
    models.ForeignKey(Issue, verbose_name=_(u'Issue'))
    models.ManyToManyField(Comment, verbose_name=_(u'Comments'))
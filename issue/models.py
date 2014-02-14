from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import Account


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


class Issue(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)

    type = models.ForeignKey(_(u'Type'), IssueType, null=True, blank=True)
    priority = models.ForeignKey(_(u'Priority'), IssuePriority,null=True,blank=True)
    assignee = models.OneToOneField(_(u'Assignee'), Account, null=True, blank=True)
    char_fields = models.ManyToManyField(_(u'Char Fields'),IssueCharField, null=True,blank=True)
    text_fields = models.ManyToManyField(_(u'Text Fields'),IssueTextField, null=True,blank=True)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)

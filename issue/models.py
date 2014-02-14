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


class IssueImageField(models.Model):
    name = models.CharField(_(u'Field Name'), max_length=128)
    value = models.ImageField(_(u'Image'), upload_to='Issue Images', null=True, blank=True)


class IssuePerson(models.Model):
    role = models.CharField(_(u'Role Name'), max_length=128)
    person = models.ForeignKey(Account, verbose_name=_(u'Person'), null=True, blank=True)


class Issue(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)

    type = models.ForeignKey(IssueType, verbose_name=_(u'Type'), null=True, blank=True)
    priority = models.ForeignKey(IssuePriority, verbose_name=_(u'Priority'), null=True, blank=True)
    assignee = models.OneToOneField(Account, verbose_name=_(u'Assignee'), null=True, blank=True)

    char_fields = models.ManyToManyField(IssueCharField, verbose_name=_(u'Char Fields'), null=True, blank=True)
    text_fields = models.ManyToManyField(IssueTextField, verbose_name=_(u'Text Fields'), null=True, blank=True)
    image_fields = models.ManyToManyField(IssueImageField, verbose_name=_(u'Image Fields'), null=True, blank=True)
    people = models.ManyToManyField(IssuePerson, verbose_name=_(u'People'), null=True, blank=True )

    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)

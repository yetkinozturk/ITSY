from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import Account


class Comment(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(Account)
    comments = models.ManyToManyField('self', null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Comment Date'), auto_now_add=True)


class MainConfiguration(models.Model):
    """
    Configuration model
    """

    ## Account Registration/Activation
    allow_registration = models.BooleanField(_(u'Allow Registration'),default=True,help_text=_(u'If disabled, Accounts need to be created internally'))
    active_after_registration = models.BooleanField(_(u'Accounts Active After Registration'),default=True,help_text=_(u'Enable Accounts after registration automatically'))

    ##Notifications
    email_changes_to_reporter = models.BooleanField(_(u'Notify Reporter'),default=True,help_text=_(u'Send Notification to issue reporter for every issue change'))
    email_changes_to_watchers = models.BooleanField(_(u'Notify Watchers'),default=True,help_text=_(u'Send Notification to issue watchers for every issue change'))
    email_changes_to_assignee = models.BooleanField(_(u'Notify Assignee'),default=True,help_text=_(u'Send Notification to issue assignee for every issue change'))
    email_changes_to_people = models.BooleanField(_(u'Notify People'), default=True,help_text=_(u'Send Notification to people assigned to issue for every issue change'))


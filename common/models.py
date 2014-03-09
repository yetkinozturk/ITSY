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
    allow_registration = models.BooleanField(_(u'Allow Registration'),default=True)
    active_after_registration = models.BooleanField(_(u'Accounts Active After Registration'),default=True)



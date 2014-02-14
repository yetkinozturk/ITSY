from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import Account


class Project(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)
    summary = models.TextField(_(u'Summary'), null=True, blank=True)

    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)


class Board(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)
    summary = models.TextField(_(u'Summary'), null=True, blank=True)
    project = models.ForeignKey(Project, _(u'Project'))
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)
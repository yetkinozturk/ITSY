from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import Account


class Comment(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(Account)
    comments = models.ManyToManyField('self', null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Comment Date'), auto_now_add=True)
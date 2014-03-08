from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import Account


class Comment(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(Account)
    comments = models.ManyToManyField('self', null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Comment Date'), auto_now_add=True)


class MainConfiguration(models.Model):
    email_use_tls = models.BooleanField(_(u'EMAIL_USE_TLS'),default=True)
    email_host = models.CharField(_(u'EMAIL_HOST'),max_length=1024)
    email_host_user = models.CharField(_(u'EMAIL_HOST_USER'),max_length=255)
    email_host_password = models.CharField(_(u'EMAIL_HOST_PASSWORD'),max_length=255)
    email_port = models.PositiveSmallIntegerField(_(u'EMAIL_PORT'),default=587)
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class AccountRole(models.Model):
    name = models.CharField(_(u'Role'), max_length=128)

    def __unicode__(self):
        return self.name


class AccountTeam(models.Model):
    name = models.CharField(_(u'Role'), max_length=128)

    def __unicode__(self):
        return self.name


class Account(models.Model):
    ACCOUNT_TYPES = (
        ('SA', 'Super Admin'),
        ('AD', 'Admin'),
        ('US', 'User'),
    )
    user = models.OneToOneField(User)
    role = models.ForeignKey(AccountRole, verbose_name=_(u'Role'), null=True, blank=True)
    team = models.ForeignKey(AccountTeam, verbose_name=_(u'Team'), null=True, blank=True)
    type = models.CharField(_(u'Account Type'), max_length=4, choices=ACCOUNT_TYPES, default='US')

    def __unicode__(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)


class Filter(models.Model):
    name = models.CharField(_(u'Filter Name'), max_length=128)
    query = models.CharField(_(u'Filter Query'), max_length=1024)

    def __unicode__(self):
        return self.name


class FavoriteFilters(models.Model):
    account = models.ForeignKey(Account, verbose_name=_(u'Account'))
    filters = models.ManyToManyField(Filter, verbose_name=_(u'Filters'))

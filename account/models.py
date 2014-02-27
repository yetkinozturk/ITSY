from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class AccountRole(models.Model):
    name = models.CharField(_(u'Role'), max_length=128)

    def __unicode__(self):
        return self.name


class AccountTeam(models.Model):
    name = models.CharField(_(u'Role'), max_length=128)

    def __unicode__(self):
        return self.name


# class Account(models.Model):
#     ACCOUNT_TYPES = (
#         ('SA', 'Super Admin'),
#         ('AD', 'Admin'),
#         ('US', 'User'),
#     )
#     user = models.OneToOneField(User)
#     role = models.ForeignKey(AccountRole, verbose_name=_(u'Role'), null=True, blank=True)
#     team = models.ForeignKey(AccountTeam, verbose_name=_(u'Team'), null=True, blank=True)
#     type = models.CharField(_(u'Account Type'), max_length=4, choices=ACCOUNT_TYPES, default='US')
#     follows = models.ManyToManyField('self', related_name='followers', symmetrical=False, null=True, blank=True)
#
#     def __unicode__(self):
#         return u'%s %s' % (self.user.first_name, self.user.last_name)


class AccountManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=AccountManager.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        u = self.create_user(username,password=password)
        u.is_admin = True
        u.save(using=self._db)
        return u


class Account(AbstractBaseUser):
    ACCOUNT_TYPES = (
        ('SA', 'Super Admin'),
        ('AD', 'Admin'),
        ('US', 'User'),
    )
    role = models.ForeignKey(AccountRole, verbose_name=_(u'Role'), null=True, blank=True)
    team = models.ForeignKey(AccountTeam, verbose_name=_(u'Team'), null=True, blank=True)
    type = models.CharField(_(u'Account Type'), max_length=4, choices=ACCOUNT_TYPES, default='US')
    follows = models.ManyToManyField('self', related_name='followers', symmetrical=False, null=True, blank=True)
    email = models.EmailField(verbose_name='email address',max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email',]

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Filter(models.Model):
    name = models.CharField(_(u'Filter Name'), max_length=128)
    query = models.CharField(_(u'Filter Query'), max_length=1024)

    def __unicode__(self):
        return self.name


class FavoriteFilters(models.Model):
    account = models.ForeignKey(Account, verbose_name=_(u'Account'))
    filters = models.ManyToManyField(Filter, verbose_name=_(u'Filters'))

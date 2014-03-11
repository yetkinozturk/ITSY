from django.db import models
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


class AccountManager(BaseUserManager):
    def create_user(self, email, firstname, lastname, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=AccountManager.normalize_email(email))
        user.firstname = firstname
        user.lastname = lastname
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstname, lastname, password):
        u = self.create_user(email=email,firstname=firstname,
                             lastname=lastname, password=password)
        u.is_admin = True
        u.save(using=self._db)
        return u


class Account(AbstractBaseUser):
    ACCOUNT_TYPES = (
        ('AD', 'Admin'),
        ('US', 'User'),
    )
    firstname = models.CharField(_(u'First Name'), max_length=128)
    lastname = models.CharField(_(u'Last Name'), max_length=128)
    role = models.ForeignKey(AccountRole, verbose_name=_(u'Role'), null=True, blank=True)
    team = models.ForeignKey(AccountTeam, verbose_name=_(u'Team'), null=True, blank=True)
    type = models.CharField(_(u'Account Type'), max_length=4, choices=ACCOUNT_TYPES, default='US')
    follows = models.ManyToManyField('self', related_name='followers', symmetrical=False, null=True, blank=True)
    email = models.EmailField(verbose_name='email address',max_length=255, unique=True)
    phone = models.CharField(_(u'Phone'), max_length=30, null=True, blank=True)
    im = models.CharField(_(u'IM'), max_length=255, null=True, blank=True)
    website = models.CharField(_(u'Website'),max_length=1024, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname']

    def __unicode__(self):
        return u'%s %s' % (self.firstname, self.lastname)

    def get_full_name(self):
        return u'%s %s' % (self.firstname, self.lastname)

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self): # For auth user compatibility
        return self.is_admin

    def save(self, *args, **kwargs):
        if self.is_admin:
            self.type = 'AD'
        super(Account, self).save(*args, **kwargs)

class Filter(models.Model):
    name = models.CharField(_(u'Filter Name'), max_length=128)
    query = models.CharField(_(u'Filter Query'), max_length=1024)

    def __unicode__(self):
        return self.name


class FavoriteFilters(models.Model):
    account = models.ForeignKey(Account, verbose_name=_(u'Account'))
    filters = models.ManyToManyField(Filter, verbose_name=_(u'Filters'))

import os
from itertools import count

from django.db import models
from django.core.exceptions import ValidationError
from pyvcs.backends import AVAILABLE_BACKENDS, get_backend
from pyvcs.exceptions import CommitDoesNotExist, FileDoesNotExist, FolderDoesNotExist
from autoslug import AutoSlugField

REPOSITORY_TYPES = zip(count(), AVAILABLE_BACKENDS.keys())


class CodeRepository(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')

    repository_type = models.IntegerField(choices=REPOSITORY_TYPES)

    location = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Code Repositories"

    def __unicode__(self):
        return "%s: %s" % (self.get_repository_type_display(), self.name)

    def clean(self,*args, **kwargs):
        super(CodeRepository, self).clean(*args, **kwargs)

        if not os.path.isdir(self.location):
            raise ValidationError('Location is not a valid directory')

        if self.repository_type == 1:
            try:
                from dulwich.repo import Repo,NotGitRepository
            except ImportError:
                ValidationError('You must install dulwich to use git repos')
            try:
                Repo(self.location)
            except NotGitRepository:
                raise ValidationError('Location is not a valid git repository')

        elif self.repository_type == 3:
            try:
                from mercurial import ui
                from mercurial.localrepo import localrepository as hg_repo
                from mercurial.error import RepoError
            except ImportError:
                ValidationError('You must install mercurial to use hg repos')
            try:
                hg_repo(ui.ui(),path=self.location)
            except RepoError:
                raise ValidationError('Location is not a valid mercurial repository')

    @models.permalink
    def get_absolute_url(self):
        return ('recent_commits', (), {'slug': self.slug})

    @property
    def repo(self):
        if hasattr(self, '_repo'):
            return self._repo
        self._repo = get_backend(self.get_repository_type_display()).Repository(self.location)
        return self._repo

    def get_commit(self, commit_id):
        try:
            return self.repo.get_commit_by_id(str(commit_id))
        except CommitDoesNotExist:
            return None

    def get_recent_commits(self, since=None):
        return self.repo.get_recent_commits(since=since)

    def get_folder_contents(self, path, rev=None):
        try:
            if rev is not None:
                rev = str(rev)
            return self.repo.list_directory(path, rev)
        except FolderDoesNotExist:
            return None

    def get_file_contents(self, path, rev=None):
        try:
            if rev is not None:
                rev = str(rev)
            return self.repo.file_contents(path, rev)
        except FileDoesNotExist:
            return None

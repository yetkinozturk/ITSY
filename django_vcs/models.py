from itertools import count

from django.db import models

from pyvcs.backends import AVAILABLE_BACKENDS, get_backend
from pyvcs.exceptions import CommitDoesNotExist, FileDoesNotExist, FolderDoesNotExist


REPOSITORY_TYPES = zip(count(), AVAILABLE_BACKENDS.keys())

class CodeRepository(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    repository_type = models.IntegerField(choices=REPOSITORY_TYPES)

    location = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Code Repositories"

    def __unicode__(self):
        return "%s: %s" % (self.get_repository_type_display(), self.name)

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

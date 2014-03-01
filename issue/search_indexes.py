import datetime
from haystack import indexes
from issue import models as issue_models


class IssueIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    summary = indexes.CharField(model_attr='summary')
    type = indexes.CharField(model_attr='type')
    status = indexes.CharField(model_attr='status')
    project_version = indexes.CharField(model_attr='project_version')


    def get_model(self):
        return issue_models.Issue

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

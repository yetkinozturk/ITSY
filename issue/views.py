from django.views.generic.edit import CreateView
from django.views.generic.list import ListView


class CreateIssueView(CreateView):
    pass


class CreateIssueFlow(CreateView):
    pass


class CreateIssueField(CreateView):
    page_title = ''
    page_heading = ''
    template_name = 'issue/create/issuefield.html'

    def get_context_data(self, **kwargs):
        context = super(CreateIssueField, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context
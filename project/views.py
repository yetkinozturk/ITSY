from django.views.generic.list import ListView


class ListProjectView(ListView):
    page_title = ''
    page_heading = ''
    template_name = 'project/view/list.html'

    def get_context_data(self, **kwargs):
        context = super(ListProjectView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context

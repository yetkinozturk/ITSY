from django.shortcuts import render
from django.views.generic.base import View
from common.views import LoginRequiredTemplateView


class MainDashboardView(LoginRequiredTemplateView):
    template_name = 'dashboard/main.html'

    def get(self,request):
        content = {}
        return render(request, self.template_name, content)

    def post(self,request):
        return render(request, self.template_name)

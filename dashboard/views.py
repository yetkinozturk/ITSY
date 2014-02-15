from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View


class MainDashboardView(View):
    template_name = 'dashboard/main.html'

    def get(self,request):
        return render(request, self.template_name)

    def post(self,request):
        return render(request, self.template_name)

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin


class LoginRequiredListView(LoginRequiredMixin,ListView):
    login_url = "/account/login/"


class LoginRequiredUpdateView(LoginRequiredMixin,UpdateView):
    login_url = "/account/login/"


class LoginRequiredCreateView(LoginRequiredMixin,CreateView):
    login_url = "/account/login/"


class LoginRequiredDeleteView(LoginRequiredMixin,DeleteView):
    login_url = "/account/login/"


class LoginRequiredTemplateView(LoginRequiredMixin,TemplateView):
    login_url = "/account/login/"

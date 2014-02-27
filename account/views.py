from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import FormView
from django.views.generic import View
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from account.forms import UserCreationForm,LoginForm


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'account/register.html'


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'account/login.html'



class UpdateUser(UpdateView):
    pass


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return HttpResponseRedirect("/account/login/")
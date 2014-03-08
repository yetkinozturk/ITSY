from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import get_object_or_404
from braces.views import LoginRequiredMixin, AccessMixin


class AuthorizationRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user,'type'):
            return redirect_to_login(request.get_full_path(),
                                     self.get_login_url(),
                                     self.get_redirect_field_name())
        if not request.user.is_staff and not (request.user.type == 'AD'):
            if self.raise_exception:
                raise PermissionDenied
            else:
                return redirect_to_login(request.get_full_path(),
                                         self.get_login_url(),
                                         self.get_redirect_field_name())

        return super(AuthorizationRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class LoginRequiredListView(LoginRequiredMixin, ListView):
    login_url = "/account/login/"


class LoginRequiredUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/account/login/"


class LoginRequiredCreateView(LoginRequiredMixin, CreateView):
    login_url = "/account/login/"


class LoginRequiredDeleteView(LoginRequiredMixin,AuthorizationRequiredMixin,
                              DeleteView):
    login_url = "/account/login/"
    raise_exception = True


class LoginRequiredTemplateView(LoginRequiredMixin, TemplateView):
    login_url = "/account/login/"


class UpdateSiteConfigView(AuthorizationRequiredMixin,LoginRequiredUpdateView):
    raise_exception = True
    template_name = 'common/edit/item.html'

    def get_object(self):
        obj, created = self.model.objects.get_or_create(id=1)
        return obj
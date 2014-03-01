from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from account.forms import UserCreationForm


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'account/register.html'


class UpdateUser(UpdateView):
    pass


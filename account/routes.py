from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse
from account.views import RegistrationView, LoginView, UpdateUser,LogoutView


urlpatterns = patterns('',
    url(r'^register/', RegistrationView.as_view(success_url='/')),
    url(r'^login/', 'django.contrib.auth.views.login',{'template_name': 'account/login.html'}),
    url(r'^logout/', LogoutView.as_view()),
    url(r'^update/', UpdateUser.as_view(success_url='/')),
)

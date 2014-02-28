from django.conf.urls import patterns, url
from account.views import RegistrationView, UpdateUser


urlpatterns = patterns('',
    url(r'^register/', RegistrationView.as_view(success_url='/')),
    url(r'^login/', 'django.contrib.auth.views.login',{'template_name': 'account/login.html'}),
    url(r'^logout/', 'django.contrib.auth.views.logout',{'next_page': '/account/login/'}),
    url(r'^update/', UpdateUser.as_view(success_url='/')),
)

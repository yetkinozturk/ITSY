from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from captcha.fields import CaptchaField
from account.models import Account


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)
    captcha = CaptchaField()
    class Meta:
        model = Account
        fields = ("email","role","team")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password mismatch")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account

    def clean_password(self):
        return self.initial['password']


class LoginForm(forms.Form):
    username = forms.CharField(label=_(u'Username'))
    password = forms.CharField(label=_(u'Password'),widget=forms.PasswordInput)
    captcha = CaptchaField()

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect("/")

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
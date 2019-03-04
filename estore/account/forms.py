from django import forms
from django.utils.translation import pgettext_lazy
from django.contrib.auth import forms as django_forms
from django.conf import settings
from django.utils.translation import pgettext

from ..account.models import User


class SignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput)
    email = forms.EmailField(
        error_messages={
            'unique': pgettext_lazy(
                'Registration error',
                'This email has already been registered.')})

    class Meta:
        model = User
        fields = ('email',)
        labels = {
            'email': pgettext_lazy(
                'Email', 'Email'),
            'password': pgettext_lazy(
                'Password', 'Password')}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update(
                {'autofocus': ''})

    def save(self, request=None, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        if commit:
            user.save()
        return user


class LoginForm(django_forms.AuthenticationForm):
    username = forms.EmailField(
        label=pgettext('Form field', 'Email'), max_length=75)

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)
        if request:
            email = request.GET.get('email')
            if email:
                self.fields['username'].initial = email

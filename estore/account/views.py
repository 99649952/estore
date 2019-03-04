from django.shortcuts import redirect
from django.contrib import auth
from django.template.response import TemplateResponse
from django.contrib.auth import views as django_views
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import (
    SignupForm, LoginForm)


def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user = auth.authenticate(
            request=request, email=email, password=password)
        if user:
            auth.login(request, user)
        return redirect('/')
    context = {'form': form}
    return TemplateResponse(request, 'account/signup.html', context)


def login(request):
    kwargs = {
        'template_name': 'account/login.html',
        'authentication_form': LoginForm}
    return django_views.LoginView.as_view(**kwargs)(request, **kwargs)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(settings.LOGIN_REDIRECT_URL)


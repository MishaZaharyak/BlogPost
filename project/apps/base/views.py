from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.shortcuts import reverse
from apps.base.forms import LoginForm, RegistrationForm


class LoginView(DjangoLoginView):
    form_class = LoginForm

    def get_success_url(self):
        return reverse("post:list")


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'

    def get_success_url(self):
        return reverse("post:list")

    def form_valid(self, form):
        self.object = form.save()
        auth_login(self.request, self.object.usermodel_ptr)
        return HttpResponseRedirect(self.get_success_url())

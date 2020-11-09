from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from apps.user.models import VisitorModel


class LoginForm(AuthenticationForm):
    """ Visitor user login form """
    def clean(self):
        """ check if Visitor user exist and if password is valid """
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            try:
                visitor = VisitorModel.objects.get(email=email)
            except VisitorModel.DoesNotExist:
                raise self.get_invalid_login_error()
            else:
                if not visitor.check_password(password):
                    raise self.get_invalid_login_error()
                else:
                    self.user_cache = visitor.usermodel_ptr

            self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class RegistrationForm(UserCreationForm):
    """ Visitor user registration form """
    class Meta:
        model = VisitorModel
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'photo')

    def clean_email(self):
        """ check if given email is not taken """
        email = self.cleaned_data.get("email")
        try:
            visitor = VisitorModel.objects.get(email=email)
        except VisitorModel.DoesNotExist:
            return email
        else:
            self.add_error('email', 'Email already in use')
            raise forms.ValidationError('')

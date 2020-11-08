from django import forms
from apps.user.models import UserModel, VisitorModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('email', "first_name", "last_name", "photo")


class VisitorForm(forms.ModelForm):
    class Meta:
        model = VisitorModel
        fields = ('email', "first_name", "last_name", "photo")

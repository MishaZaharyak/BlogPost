from django import forms
from apps.user.models import UserModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('email', "first_name", "last_name", "photo")

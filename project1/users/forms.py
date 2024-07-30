from django import forms
from django.contrib.auth.models import User

class Loginform(forms.Form):
    username = forms.CharField(required=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class UserCreationModel(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("Passwords bir-biriga to'g'ri kelishi kerak")
        return data['password2']




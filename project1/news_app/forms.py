from django import forms
from .models import ContactModel, CommentModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['message']

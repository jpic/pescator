from django import forms

from .models import Entry


class EntryCreateForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('name', 'email', 'body')

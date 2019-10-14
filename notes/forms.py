from . import models
from django import forms

class NotesCreationForm(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ('title', 'content')

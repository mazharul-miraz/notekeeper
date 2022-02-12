import imp
from django import forms

class noteForm(forms.Form):
    note_title= forms.CharField(max_length=100)
    note_content=forms.CharField(max_length=150)
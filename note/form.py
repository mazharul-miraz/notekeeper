from django import forms
from .models import noteModel

class noteForm(forms.ModelForm):
    # note_title= forms.CharField(max_length=100)
    # note_content=forms.CharField(max_length=150)
    
    class Meta:
        model = noteModel
        fields = "__all__"
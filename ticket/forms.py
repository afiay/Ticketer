from tkinter import Image
from django import forms
from .models import Replie

class ReplieModelForm(forms.ModelForm):
    class Meta:
        model = Replie
        fields = ['ticket', 'body']
        widgets = {
            'ticket': forms.HiddenInput(),
            'body': forms.Textarea(attrs={'placeholder': 'Write your comment here...'}),
        }
class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
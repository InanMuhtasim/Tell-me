from django import forms
from .models import Confession

class ConfessionForm(forms.ModelForm):
    class Meta:
        model = Confession
        fields = ['letter_receiver', 'message', 'key']

    # You can add custom validation or widgets here if needed
    letter_receiver = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input is-rounded', 'placeholder': 'Enter recipient name'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'textarea is-rounded', 'placeholder': 'Enter your confession message'})
    )
    key = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'input is-rounded', 'placeholder': 'Create a key'})
    )
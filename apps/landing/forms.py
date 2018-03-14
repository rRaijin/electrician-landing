from django import forms


class TelegrammForm(forms.Form):
    name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your name..'}))
    phone = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your phone..'}))
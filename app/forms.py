from django import forms


class CowsayForm(forms.Form):
    text = forms.CharField(max_length=100)

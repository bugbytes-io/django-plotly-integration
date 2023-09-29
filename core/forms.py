from django import forms

class PoolForm(forms.Form):
    network = forms.DateField(widget=forms.TextInput())
    token0 = forms.DateField(widget=forms.TextInput())
    token1 = forms.DateField(widget=forms.TextInput())
    fee_tier = forms.DateField(widget=forms.TextInput())

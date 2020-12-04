from django import forms


class SEARCH(forms.Form):
    search=forms.CharField(widget=forms.TextInput,label='')


    
from django import forms


class CountForm(forms.Form):
    count = forms.IntegerField(label="Count", min_value=1, max_value=100)

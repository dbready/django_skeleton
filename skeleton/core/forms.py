from django import forms


class CalcForm(forms.Form):
    num_one = forms.IntegerField(label="Left number")
    num_two = forms.IntegerField(label="Right number")

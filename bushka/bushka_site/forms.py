from django import forms

class CheckBoxInputForm(forms.Form):
    weapons = forms.CheckboxInput()
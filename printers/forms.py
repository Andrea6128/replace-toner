from django import forms
from .models import Main


class Subscribe(forms.Form):
    # Email = forms.EmailField()
    pass
    # def __str__(self):
        # return self.Email

class MainForm(forms.ModelForm):
    class Meta:
        model = Main
        # fields that should be visible on the form template:
        fields = ('roomNumber', 'printerName', 'tonerColor', )
        # fields = forms.CharField(label="Your label")

        def __str__(self):
            return self.fields

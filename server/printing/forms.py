from django import forms
import re

class SubmissionForm(forms.Form):
    gcode = forms.FileField(label='File with gcode for the printer')
    token = forms.CharField(label='Verification token')

    def is_valid(self):
        return super().is_valid() and re.fullmatch(r'.+\.gcode', self.cleaned_data['gcode'].name) is not None

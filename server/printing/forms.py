from django import forms


class SubmissionForm(forms.Form):
    gcode = forms.FileField(label='File with gcode for the printer')
    token = forms.CharField(label='Verification token')

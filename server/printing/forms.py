from django import forms


class SubmissionForm(forms.Form):
    token = forms.CharField(label='Verification token')

from django.shortcuts import render

from .forms import SubmissionForm
from .controllers import store_file, log

def submit_gcode(request):
    if request.method == 'POST':
        print()
        form = SubmissionForm(request.POST, request.FILES)
        # Temporary token.
        # TODO: enhance security
        if form.is_valid() and form['token'].value() == 'uKh+1U1js"Zt]k,':
            store_file(request.FILES['gcode'])
    else:
        form = SubmissionForm()

    content = {
        'form': form,
    }
    return render(request, 'submit-gcode.html', content)

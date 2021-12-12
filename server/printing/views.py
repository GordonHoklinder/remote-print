from django.shortcuts import render

from .forms import SubmissionForm
from .controllers import store_file, log

def submit_gcode(request):
    if request.method == 'POST':
        print()
        form = SubmissionForm(request.POST, request.FILES)
        # Temporary token.
        # TODO: enhance security
        log(str(form['token'].field))
        log(str(form))
        if form.is_valid() and form['token'].field == 'uKh+1U1j%s"Zt]k,':
            store_file(request.FILES['gcode'])
    else:
        form = SubmissionForm()

    content = {
        'form': form,
    }
    return render(request, 'submit-gcode.html', content)

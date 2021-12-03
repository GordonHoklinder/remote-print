from django.shortcuts import render

from .forms import SubmissionForm
from .controllers import store_file

def submit_gcode(request):
    if request.method == 'POST':
        print()
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            store_file(request.FILES['gcode'])
    else:
        form = SubmissionForm()

    content = {
        'form': form,
    }
    return render(request, 'submit-gcode.html', content)

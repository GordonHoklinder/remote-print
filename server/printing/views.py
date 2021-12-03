from django.shortcuts import render

from .forms import SubmissionForm

def submit_gcode(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = SubmissionForm()

    content = {
        'form': form,
    }
    return render(request, 'submit-gcode.html', content)

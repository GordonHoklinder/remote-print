from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .forms import SubmissionForm
from .controllers import store_file, log, load_print_history, get_printing_state

@login_required(login_url='/login/')
def submit_gcode(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid() and get_printing_state() == 'idle':
            store_file(request.FILES['gcode'])
    else:
        form = SubmissionForm()

    content = {'form': form, 'printer_state': get_printing_state()}
    return render(request, 'index.html', content)


@login_required(login_url='/login/')
def show_history(request):
    content = {'history': load_print_history()}
    return render(request, 'history.html', content)


def login_request(request):
    next_page = request.GET.get('next')
    print(next_page)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
            print(next_page)
            if next_page is not None:
                return redirect(next_page)
            else:
                return redirect('/')
    else:
        form = AuthenticationForm()

    content = {'form': form,}
    return render(request, 'form.html', content)


def logout_request(request):
    logout(request)
    return redirect('/')


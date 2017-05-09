from django.shortcuts import render, redirect
from .forms import EditorForm


def index(request):
    return render(request, 'LS/index.html')


def tasks(request):
    if request.method == 'POST':
        form = EditorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['text'])
            return redirect('/')
    else:
        form = EditorForm()

    return render(request, 'LS/tasks.html', {'editor': form})


def contacts(request):
    return render(request, 'LS/contacts.html')


def about(request):
    return render(request, 'LS/about.html')
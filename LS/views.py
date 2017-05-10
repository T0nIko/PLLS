from django.shortcuts import render, redirect


def index(request):
    return render(request, 'LS/index.html')


def tasks(request):
    res = {}
    if request.method == 'POST':
        for key, val in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                res[key] = val

        return render(request, 'LS/tasks.html')

    return render(request, 'LS/tasks.html')


def contacts(request):
    return render(request, 'LS/contacts.html')


def about(request):
    return render(request, 'LS/about.html')
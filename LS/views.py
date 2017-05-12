from django.shortcuts import render

from .utilities import *


def index(request):
    return render(request, 'LS/index.html')


def tasks(request):
    if request.method == 'POST':
        res = {}
        for key, val in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                res[key] = val

        fp = FileProcessor()
        # fn = create_file(res['code'], 1, 'py')
        # out = execute_file(fn, 'py')
        # res = check_res(out, 1)
        print(fp.filechecker_wrapper(res['code'], 1, 'py', 1))
        return render(request, 'LS/tasks.html')

    return render(request, 'LS/tasks.html')


def contacts(request):
    return render(request, 'LS/contacts.html')


def about(request):
    return render(request, 'LS/about.html')

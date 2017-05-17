from django.shortcuts import render

from .utils import *


def index(request):
    return render(request, 'LS/index.html')


def tasks(request):
    fp = FileProcessor()

    if request.method == 'POST':
        res = {}
        for key, val in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                res[key] = val

        mode = 'py' if len(res) == 3 else 'cpp'
        out = fp.filechecker_wrapper(res['code'], res['task-id'], mode, 1)

        return render(request, 'LS/results.html', {'answer': out[0], 'output': out[1], 'error': out[2]})

    return render(request, 'LS/tasks.html', {'last_id': last_task_id(), 'task_list': get_task_list()})


def contacts(request):
    return render(request, 'LS/contacts.html')


def about(request):
    return render(request, 'LS/about.html')

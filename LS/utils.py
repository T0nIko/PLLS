import subprocess

from .config import *
from .models import Code


class FileProcessor():
    def __init__(self):
        pass

    def _execute_file(self, file_name, mode):
        cc = ""
        if mode == 'py':
            cc = "{4} {2}{3}{0}.{1}".format(file_name, mode, SRC_PATH, PY_PATH, PY_EXEC)
        elif mode == 'cpp':
            cc = "cd src_exec/cpp/build && {4} {5} {0} ../{0}.{1} && ./{0}".format(file_name, mode, SRC_PATH,
                                                                                   CPP_PATH, CPP_EXEC, CPP_FLAGS)

        sp = subprocess.run(cc, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=TIMEOUT_SEC)

        output = sp.stdout
        error = sp.stderr

        return output, error

    def _create_file(self, data, task_id, mode, user_id):
        file_name = '{}-{}'.format(task_id, user_id)
        file_name_full = '{}.{}'.format(file_name, mode)

        if mode == 'py':
            f = open(SRC_PATH + PY_PATH + file_name_full, 'w+')
        else:
            f = open(SRC_PATH + CPP_PATH + file_name_full, 'w+')

        f.write(data)
        f.close()

        return file_name

    def _check_res(self, res, task_id):
        task = Code.objects.get(id=task_id)
        c_res = res[0].decode('utf-8').replace('\n', '').replace('\r', '')
        c_err = res[1].decode('utf-8').replace('\n', ' ').replace('\r', '')
        if c_res == task.c_answer:
            return True, c_res, c_err
        else:
            return False, c_res, c_err

    def filechecker_wrapper(self, data, task_id, mode, uid):
        return self._check_res(self._execute_file(self._create_file(data, task_id, mode, uid), mode), task_id)


def last_task_id():
    last = Code.objects.latest('id')
    return last.id


def get_task_list():
    tasks = Code.objects.all()
    task_list = [[task.id, task.task_name, task.text] for task in tasks]
    return task_list

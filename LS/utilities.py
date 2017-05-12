import subprocess

from .config import *
from .models import Code


class FileProcessor():
    def __init__(self):
        pass

    def execute_file(self, file_name, mode):
        cc = ""
        if mode == 'py':
            cc = "{4} {2}{3}{0}.{1}".format(file_name, mode, SRC_PATH, PY_PATH, PY_EXEC)
        elif mode == 'cpp':
            cc = "{4} {5} {0} {2}{3}{0}.{1} && {2}{3}{0}".format(file_name, mode, SRC_PATH, CPP_PATH, CPP_EXEC,
                                                                 CPP_FLAGS)

        sp = subprocess.run(cc, shell=True, stdout=subprocess.PIPE, timeout=TIMEOUT_SEC)

        output = sp.stdout

        return output

    def create_file(self, data, task_id, mode, user_id):
        file_name = '{}-{}'.format(task_id, user_id)
        file_name_full = '{}.{}'.format(file_name, mode)

        if mode == 'py':
            f = open(SRC_PATH + PY_PATH + file_name_full, 'w+')
        else:
            f = open(SRC_PATH + CPP_PATH + file_name_full, 'w+')

        f.write(data)
        f.close()

        return file_name

    def check_res(self, res, task_id):
        task = Code.objects.get(id=task_id)
        c_res = res.decode('utf-8').replace('\n', '').replace('\r', '')

        if c_res == task.c_answer:
            return True
        else:
            return False

    def filechecker_wrapper(self, data, task_id, mode, uid):
        return self.check_res(self.execute_file(self.create_file(data, task_id, mode, uid), mode), task_id)

import subprocess, os, datetime, re
from . import models


def execute_file(file_name, mode):
    cc = ""
    if mode == 'py':
        cc = "python3 {0}.{1}".format(file_name, mode)
    elif mode == 'cpp':
        cc = "g++ -o {0} {0}.{1} && ./{0}".format(file_name, mode)

    sp = subprocess.run(cc, shell=True, stdout=subprocess.PIPE)
    output = sp.stdout

    return output


def create_file(data, task_id):
    file_name = '{}-{}'.format(task_id, datetime.datetime)

    f = open(file_name, 'w+')
    f.write(data)
    f.close()

    return file_name


def check_res(res, task_id):
    compiled_pattern = re.compile(r'(\\b\\n|\\n)+| ')

    task = models.Code.objects.get(id==task_id)

    if re.sub(compiled_pattern, "", res) == re.sub(compiled_pattern, "", task.c_answer):
        return True, res
    else:
        return False, res


def filechecker_wrapper(data, task_id, mode):
    return check_res(execute_file(create_file(data, task_id), mode), task_id)

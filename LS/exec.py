import subprocess


def execute_file(file_name, mode):
    cc = ""
    if mode == 'py':
        cc = "python3 {}.{}".format(file_name, mode)
    elif mode == 'cpp':
        cc = "g++ -o {0} {0}.{1} && ./{0}".format(file_name, mode)

    sp = subprocess.run(cc, shell=True, stdout=subprocess.PIPE)
    output = sp.stdout
    return output


def check_res(file_output):
    pass

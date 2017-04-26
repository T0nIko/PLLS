import subprocess


def execute_file(file_name, mode):
    if mode == 'py':
        cc = "python3 {}.py".format(file_name)
        sp = subprocess.run(cc, shell=True, stdout=subprocess.PIPE)
        output = sp.stdout
        return output


print(execute_file('test_exec', 'py'))

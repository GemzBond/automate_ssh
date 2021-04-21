import platform 
import os
from paramiko import SSHClient, AutoAddPolicy, client
from rich import print, pretty, inspect
pretty.install()

with open("ip_list_copy.txt") as file:
    dump = file.read()
    dump = dump.splitlines()
    current_os = platform.system().lower()

    if current_os == "windows":
        param = "-n"
        output = "\Desktop\output.txt"
        homedir = os.environ['USERPROFILE']
    else:
        param = "-c"
        output = "/Desktop/output.txt"
        homedir = os.environ['HOME']
    
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    for ip in dump:
        print(ip)
        client.connect(ip, username='your_user', password='your_pass')
        stdin, stdout, stderr = client.exec_command(f'ping {param} 3 x.x.x.x')
        res = f'STDOUT: |{ip}| {stdout.read().decode("utf8")}'
        file = open(f'{homedir}/Desktop/output.txt', 'a')
        file.write(res)
        file.close()







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
    
    

    for ip in dump:
        print(ip)
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(ip, username='your_username', password='your_pass')
        stdin, stdout, stderr = client.exec_command(f'ping -c 3 x.x.x.x')
        res = f'STDOUT: |{ip}| {stdout.read().decode("utf8")}'
        print(f'STDERR: {stderr.read().decode("utf8")}')
        file = open(f'{homedir}/Desktop/output.txt', 'a')
        file.write(res)
        file.close()
    
    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    # Close the client itself
    client.close()







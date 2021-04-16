import os
import platform

with open("ip_list.txt") as file:
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
        res = os.popen(f"ping {ip} {param} 3").read()
        file = open(f'{homedir}{output}', 'a')
        file.write(res)
        file.close()


import paramiko

host = "172.168.2.1"
port = 22
username = "gplink"
password = "GPLinkAdm!n"

command = "ping google.com"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
ssh.close()

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)


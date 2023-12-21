
#!/bin/python3

import paramiko
import sys

nbyts = 4096
hostname = input("insert IP: ")
port = 22
username = input("insert username: ")
password = input("password: ")
command = '''
sudo apt-get update -y
echo hostname + "paramiko" >> /etc/hosts
mkdir /home/username/Desktop/Project/new
cd /home/username/Desktop/Project/new
touch newfile.txt
echo "hello world" > newfile.txt'''



client = paramiko.Transport((hostname, port))
client.connect(username=username, password=password)

sudout_data = []
stderr_data = []
session = client.open_channel(kind='session')
session.exec_command(command)

session.close()
client.close()

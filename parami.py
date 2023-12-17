
#!/bin/python3

import paramiko
import sys

nbyts = 4096
hostname = '193.168.1.1'
port = 22
username = 'lilit'
password = 'rootroot'
command = '''
sudo apt-get update -y
echo "192.168.1 213 ubuntu_left" >> /etc/hosts
mkdir /home/lilit/Desktop/Project/new
cd /home/lilit/Desktop/Project/new
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

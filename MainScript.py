
#!/bin/python3

import os

choice = input("""
Menu:
1. Discover all IPs in network with Nmap
2. Install full packages on this machine
3. Install Jenkins Master on a remote machine
4. Run Ansible-Playbook  
""")

if choice == "1":
    os.system("nmap -sn 192.168.1.0/24")
elif choice == "2":
    package = input("""Which package do you want to install? Only one at a time: 
1. python3
2. net-tools
3. passwd
4. hostname
""")
    if package == "python3":
        os.system("sudo apt-get install python3")
    elif package == "net-tools":
        os.system("sudo apt-get install net-tools")
    elif package == "passwd":
        os.system("sudo apt-get install passwd")
    elif package == "hostname":
        os.system("sudo apt-get install hostname")
    else:
        print("please enter the exact name of the package")
elif choice == "3":
    os.system("bash sshpass.sh")
elif choice == "4":
    os.system("ansible-playbook playbook1.yaml")

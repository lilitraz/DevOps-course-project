#!/bin/bash


echo -e "Please enter hostname: "
read hostname
echo -e "Please enter an IP of the machine you want to install Jenkins on: "
read remoteip
ssh-copy-id $remoteip
ssh $hostname@$remoteip '\
sudo apt install openjdk-11-jdk -y
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install jenkins -y
sudo systemctl status jenkins'

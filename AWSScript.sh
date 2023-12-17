#!/bin/bash


echo -e "Welcome to AWS menu!\nChoose one action:\n1. Build 2 EC2 instances\n2. Stop/Start instance\n3. Destroy instance\n4. Show all instances"

read choice
if [ $choice == "1" ]
then
	python3 build_2.py
elif [ $choice == "2" ]
then
	echo "What do you want to do? choose stop/start"
	read stosta
	if [ $stosta == "start" ]
	then
		echo "What's the instance's ID you want to start? "
		read startid
		aws ec2 start-instances --instance-ids $startid
	elif [ $stosta == "stop" ]
	then
		echo "What's the instance's ID you want to stop?"
		read stopid
		aws ec2 stop-instances --instance-ids $stopid
	fi
elif [ $choice == "3" ]
then
	python3 destroy.py
elif [ $choice == "4" ]
then
	aws ec2 describe-instances --query "Reservations[*].Instances[*].[InstanceId,State.Name]" --output table
else
	echo "please enter 1-5 only!"

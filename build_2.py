#!/bin/pyton3

import boto3
import os

typim = input("insert machine type: ")
ami = input("insert image ID: ")
keyname = input("insert key name: ")
secgroup = input("insert security group: ")

ec2 = boto3.client('ec2')


instance_type = typim
ami_id = ami
key_name = keyname
security_group_ids = [secgroup]


response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=security_group_ids,
    MinCount=1,
    MaxCount=2
)


instance_id = response['Instances'][0]['InstanceId']
print(f'Instance ID: {instance_id}')


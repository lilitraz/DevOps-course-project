#!/bin/bash


import boto3


instance_id = input("insert instance ID to destroy: ")
ec2 = boto3.resource('ec2')

instance = ec2.Instance(instance_id)
response = instance.terminate()

print(f"Instance {instance_id} termination response: {response}")

#!/usr/bin/python3

import boto3
#boto3 is the official AWS software development kit(SDK) for python. python can interact with aws services using boto3
ec2 = boto3.client('ec2')

response = ec2.describe_instances()

for reservation in response['Reservations']:
  for instance in reservation['Instances']:
    instance_id = instance['InstanceId']
    state = instance['State']['Name']
    print(instance_id, Name)

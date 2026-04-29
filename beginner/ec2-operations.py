#####SCRIPT-1###########
#####To LIST ALL THE EC2 INSTANCES IN MY ACCOUNT ALONG WITH THEIR CURRENT STATE####

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
    
------------------------------------------------------------------------------------------------------------------------------
#####SCRIPT-2###########
#####To LIST RUNNING, STOPPED & TERMINATED EC2 INSTANCES SEPARATELY####

#!/usr/bin/python3
import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()

running_instances = []
stopped_instances = []
terminated_instances = []

for reservation in response['Reservations']:
  for instance in reservation['Instances']:
    instance_id = instance['InstancdId']
    state = instance['State']['Name']
    if state == 'running':
      running_instances.append(instance_id)
    if state == 'stopped':
      stopped_instances.append(instance_id)
    if state == 'terminate':
      terminated_instances.append(instance_id)

print("Below are the EC2 instances in running state:")
print(running_instances)
print("Below are the EC2 instances in stopped state:")
print(stopped_instances)
print("Below are the EC2 instances in terminated state:")
print(terminated_instances)



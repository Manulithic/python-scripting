#!/usr/bin/python3

import boto3
import json

file = "inventory.json"
preprod_resources = []
prod_resources = []
with open(file, "r") as inventors:
    data = json.load(inventors)
    for instance in data:
        if instance['environment'] == 'preprod':
            preprod_resources.append(instance)
        else:
            prod_resources.append(instance)
print("preprod_resources")
for instance in preprod_resources:
    print(instance['name'],instance['instance_id'],instance['state'])
print("prod_resources")
for instance in prod_resources:
    print(instance['name'],instance['instance_id'],instance['state'])

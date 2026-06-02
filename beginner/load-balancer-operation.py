#################SCRIPT-1#######################
##############LIST PUBLIC AND PRIVATE LOAD BALANCERS##################
#!/usr/bin/python3

import sys
import boto3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

elbv2 = boto3.client('elbv2')

response = elbv2.describe_load_balancers()

public_load_balancers = []
private_load_balancers = []
for balancer in response['LoadBalancers']:
    schema = balancer['Scheme']
    if schema == 'internet-facing':
        public_load_balancers.append(balancer)
    else:
        private_load_balancers.append(balancer)

logger.info("Public Load Balancers")
for balancer in public_load_balancers:
    print(balancer['LoadBalancerName'], balancer['LoadBalancerArn'])

logger.info("Private Load Balancers")
for balancer in private_load_balancers:
    print(balancer['LoadBalancerName'], balancer['LoadBalancerArn'])

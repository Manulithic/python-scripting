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

-------------------------------------------------------------------------------------------------------------------------
#################SCRIPT-2#######################
##############LIST DETAILS OF LB BY IT'S NAME AS INPUT##################

#!/usr/bin/python3

import sys
import boto3
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

lbs = sys.argv[1:]
elbv2 = boto3.client('elbv2')

response = elbv2.describe_load_balancers()

logger.info("fetching load balancer details")

for lb in lbs:
    found = False
    for balancer in response['LoadBalancers']:
        arn = balancer['LoadBalancerArn']
        scheme = balancer['Scheme']
        lbtype = balancer['Type']
        if balancer['LoadBalancerName'] == lb:
            found = True
            print(lb, arn, scheme, lbtype)
    if not found:
        logger.info(f"load balancer is not found")

-------------------------------------------------------------------------------------------------------------------------
#################SCRIPT-3#######################
##############LIST PORTS CONFIGURED ON LB BY TAKING IT'S NAME AS INPUT##################

#!/usr/bin/python3

import sys
import boto3
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

lbs = sys.argv[1:]
elbv2 = boto3.client('elbv2')

response = elbv2.describe_load_balancers()

for lb in lbs:
    found = False
    for balancer in response['LoadBalancers']:
        lb_arn = balancer['LoadBalancerArn']
        if balancer['LoadBalancerName'] == lb:
            found = True
            listeners = elbv2.describe_listeners(LoadBalancerArn=lb_arn)
            logger.info(f"fetching listeners for {lb}:")
            for listener in listeners['Listeners']:
                port = listener['Port']
                print(port)
    if not found:
        logger.info(f"load balancer {lb} not found")

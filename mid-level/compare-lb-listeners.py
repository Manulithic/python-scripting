#!/usr/bin/python3


import boto3
import sys
import logging

elbv2 = boto3.client('elbv2')
response = elbv2.describe_load_balancers()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#gets amazon resource number for lbname passed as input
def get_lb_arn(lbname):
    for balancer in response['LoadBalancers']:
        if balancer['LoadBalancerName'] == lbname:
            arn = balancer['LoadBalancerArn']
            logger.info(f"found the lb {lbname} with arn {arn}")
            return arn
    logger.error(f"load balancer {lbname} not found")


#returns all the ports(listeners) for a load balancer whose arn is passed as input
def get_lb_listeners(lb_arn):
    ports = []
    found = False
    listeners = elbv2.describe_listeners(LoadBalancerArn=lb_arn)
    logger.info(f"fetching ports for for {lb_arn}")
    for listener in listeners['Listeners']:
        found = True
        port = listener['Port']
        protocol = listener['Protocol']
        ports.append((port,protocol))
    if not found:
        logger.info(f"no ports found for the load balancer with arn {lb_arn}")
    return ports

#compares listeners of source lb and target lb. returns missing ports in target lb as output
def compare_listeners(source_listeners, target_listeners):
    missing = []
    for listener in source_listeners:
        if listener not in target_listeners:
            missing.append(listener)
    return missing

def  main():
    source_lb = sys.argv[1]
    target_lb = sys.argv[2]
    source_lb_arn = get_lb_arn(source_lb)
    target_lb_arn = get_lb_arn(target_lb)

    logger.info(f"fetching listeners for lb {source_lb}")
    source_lb_listeners = get_lb_listeners(source_lb_arn)
    print(source_lb_listeners)

    logger.info(f"fetching listeners for lb {target_lb}")
    target_lb_listeners = get_lb_listeners(target_lb_arn)
    print(target_lb_listeners)

    missing = compare_listeners(source_lb_listeners, target_lb_listeners)
    logger.info(f"these ports are missing from {target_lb}")
    print(missing)

if __name__ == "__main__":
    main()

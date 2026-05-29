#!/usr/bin/python3.6

import json
import logging

file = "alerts.json"
logging.basicConfig(level=logging.INFO)
logger = logging.getlogger()

with open(file, "r") as alerts:
  data = json.read(alerts)
  found = False
  for alert in data:
    severity = alert['severity']
    alertid = alert['alert_id']
    sourceip = alert['source_ip']
    status = alert['status']
    if severity == "HIGH":
      found = True
      print(alertid, severity, sourceip, status)
    logger.info("ALERT: ADDRESS THESE ALERTS IMMEDIATELY!")
  if not found:
    logger.info("NO SERVER ALERTS")
    

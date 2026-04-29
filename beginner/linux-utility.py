####SCRIPT-1#######
####SERVICE STATUS CHECK#####
#!/usr/bin/python3
import subprocess
import sys

services = sys.argv[1:]   #service list will be passed as command line argument

for service in services:
  cmd = ["systemctl", "status", service]
  status = subprocess.run(cmd, capture_output=True, text=True)
  print(status.stdout)

#usage: python3 linux-utility.py apache2 nginx

----------------------------------------------------------------------------------------

  
  


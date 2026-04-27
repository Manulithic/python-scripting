#!/usr/bin/python3
import requests
import sys

url = sys.argv[1]   #if you want to pass the url as command line arguments
#url = "https://www.google.com" if you want to hard code the url

response = requests.get(url, timeout=5)
result = response.status_code

try:
  if result == 200:
    print("Healt check is passed:", result)
    sys.exit(0) #success
  else:
    print("Health check is failed:", result)
    sys.exit(2)  #warning
except requests.exceptions.RequestException:
    print("Service Unreachable")
    sys.exit(1) #failure

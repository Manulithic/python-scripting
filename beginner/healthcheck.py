#!/usr/bin/python3
import requests
import sys

urls = sys.argv[1:]   #if you want to pass the url as command line arguments [ e.g. python3 healthcheck.py https://www.google.com https://www.facebook.com ]
#url = sys.argv[1] if you're just passing one url for health check
#url = "https://www.google.com" if you want to hard code the url
#urls = ["https://www.google.com", "https://www.facebook.com"] if you want to hard code multiple urls

if len(urls) < 1:
  print("Error: No URLs included for health check")
  print("Example: python3 healthcheck.py https://www.google.com https://www.example.com")

exit_code = 0

for url in urls:
  try:
    response = requests.get(url, timeout=5)
    result = response.status_code
    response_time = requests.get(url, timeout=5).elapsed.total_seconds()
    if result == 200:
      print(url, "is up and status code is", result, "and response time is:", response_time)
    else:
      print(url, "is down and status code is", result, "and response time is:", response_time)
      exit_code = 1
  except requests.exceptions.RequestException:
    print("Service Unreachable")

sys.exit(exit_code)

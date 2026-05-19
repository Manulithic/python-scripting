#!/usr/bin/python3

import requests
import sys

url = "https://jsonplaceholder.typicode.com/users"
employees = sys.argv[1:]
response = requests.get(url, timeout=10)
data = response.json()

for employee in employees:
    found = False
    for user in data:
        if user['name'] == employee:
            found = True
            print("Employee Details:")
            print(f"Name: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Address: {user['address']['city']}")
            print(f"Zipcode: {user['address']['zipcode']}")
    if not found:
        print("ERROR: Employee you've entered is not a part of this organisation")

# tenant suspension

# 1.    read id from text file
# 2.    line -> suspend

import requests
from requests.auth import HTTPBasicAuth
import json
from glob import glob
from getpass import getpass

# auth code

username = f"management/{input('Username: ')}"
password = getpass("Password: ")

print("auth done.")

# read file

with open('file.txt') as file:
    tenants = file.readlines()

# define request headers

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

#suspension request

payload = {'status': 'SUSPENDED'}

# go through lines

count = 0
for line in tenants:
    count += 1
    line = line.strip()

    # tenant suspension

    print(f'tenant {count}: {line} suspending')

    url = f'http://localhost:8111/tenant/tenants/{line}'

    response = requests.request('PUT', url, headers = headers, data = json.dumps(payload), auth=(username, password))

    print(response.text)
